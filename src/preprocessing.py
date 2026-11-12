import numpy as np
import nibabel as nib
from scipy.ndimage import gaussian_filter
from scipy.signal import butter, filtfilt

def smooth_spatial_image(img, fwhm_mm):
    # Apply 3D Gaussian Spatial Smoothing to each 3D frame of a 4D NIfTI image.
    data = img.get_fdata()
    affine = img.affine
    voxel_sizes = img.header.get_zooms()[:3]
    
    sigmas = [fwhm_mm / (2.3548 * vs) for vs in voxel_sizes]
    
    smoothed_data = np.zeros_like(data)
    if data.ndim == 4:
        for t in range(data.shape[3]):
            smoothed_data[..., t] = gaussian_filter(data[..., t], sigma=sigmas)
    else:
        smoothed_data = gaussian_filter(data, sigma=sigmas)
        
    return nib.Nifti1Image(smoothed_data, affine)

def highpass_temporal_filter(img, tr, cutoff_hz=0.01):
    # Apply a voxel-wise temporal high-pass Butterworth filter.
    data = img.get_fdata()
    affine = img.affine
    shape = data.shape
    
    if data.ndim != 4:
        raise ValueError("High-pass filtering requires a 4D timeseries dataset.")
        
    nyq = 0.5 * (1.0 / tr)
    normal_cutoff = cutoff_hz / nyq
    b, a = butter(5, normal_cutoff, btype='high', analog=False)
    
    flat_data = data.reshape(-1, shape[3])
    filtered_flat = np.zeros_like(flat_data)
    
    for idx in range(flat_data.shape[0]):
        if np.std(flat_data[idx, :]) > 1e-3:
            filtered_flat[idx, :] = filtfilt(b, a, flat_data[idx, :])
        else:
            filtered_flat[idx, :] = flat_data[idx, :]
            
    filtered_data = filtered_flat.reshape(shape)
    return nib.Nifti1Image(filtered_data, affine)