import numpy as np
import pandas as pd
import nibabel as nib

def calculate_fd(motion_parameters_array, r_radius=50.0):
    # Compute Framewise Displacement (FD) using the Power (2012) framework.
    motion_data = motion_parameters_array.copy()
    motion_data[:, 3:] = motion_data[:, 3:] * r_radius
    
    diffs = np.abs(np.diff(motion_data, axis=0))
    fd = np.sum(diffs, axis=1)
    return np.insert(fd, 0, 0.0)

def calculate_dvars(img):
    # Compute temporal derivative of RMS variance over voxels (DVARS).
    data = img.get_fdata()
    shape = data.shape
    flat_data = data.reshape(-1, shape[3])
    
    diff = np.diff(flat_data, axis=1)
    dvars = np.sqrt(np.mean(diff ** 2, axis=0))
    return np.insert(dvars, 0, 0.0)

def calculate_tsnr(img):
    # Compute temporal signal-to-noise ratio map.
    data = img.get_fdata()
    mean_volume = np.mean(data, axis=-1)
    std_volume = np.std(data, axis=-1)
    std_volume[std_volume == 0] = 1e-6
    tsnr = mean_volume / std_volume
    return tsnr