import numpy as np

def extract_roi_timeseries(img, rois_coords, mask_img, radius_voxels=2):
    # Extract mean temporal activity from defined spatial coordinates.
    data = img.get_fdata()
    mask = mask_img.get_fdata() > 0
    roi_signals = []
    
    for coord in rois_coords:
        cx, cy, cz = coord
        x_idx = slice(max(0, cx - radius_voxels), min(data.shape[0], cx + radius_voxels + 1))
        y_idx = slice(max(0, cy - radius_voxels), min(data.shape[1], cy + radius_voxels + 1))
        z_idx = slice(max(0, cz - radius_voxels), min(data.shape[2], cz + radius_voxels + 1))
        
        sphere_subvolume = data[x_idx, y_idx, z_idx, :]
        sphere_mask = mask[x_idx, y_idx, z_idx]
        
        if np.sum(sphere_mask) > 0:
            mean_series = np.mean(sphere_subvolume[sphere_mask, :], axis=0)
        else:
            mean_series = np.mean(sphere_subvolume, axis=(0,1,2))
        roi_signals.append(mean_series)
        
    return np.array(roi_signals).T

def compute_connectivity_matrix(timeseries):
    # Generate Pearson correlation coefficient matrix.
    return np.corrcoef(timeseries.T)