import os
import numpy as np
import nibabel as nib
from skimage.filters import threshold_otsu

def validate_nifti_file(file_path):
    # Validates file existence and correct extension format.
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not (file_path.endswith('.nii') or file_path.endswith('.nii.gz')):
        raise ValueError("Invalid file type. Must be .nii or .nii.gz")
    return True

def load_fmri_image(file_path):
    # Load a 4D NIfTI functional image safely.
    validate_nifti_file(file_path)
    return nib.load(file_path)

def get_image_metadata(img):
    # Extract dimensional and voxel specifications from a NIfTI object.
    header = img.header
    zooms = header.get_zooms()
    return {
        "shape": img.shape,
        "ndim": img.ndim,
        "voxel_sizes_mm": list(zooms[:3]),
        "tr_sec": float(zooms[3]) if len(zooms) > 3 else 2.0,
        "datatype": str(header.get_data_dtype())
    }

def create_brain_mask(img):
    # Generates a dynamic 3D binary mask using Otsu global thresholding on average volume.
    data = img.get_fdata()
    mean_volume = np.mean(data, axis=-1) if img.ndim == 4 else data
    thresh = threshold_otsu(mean_volume)
    binary_mask = mean_volume > thresh
    return nib.Nifti1Image(binary_mask.astype(np.uint8), img.affine)