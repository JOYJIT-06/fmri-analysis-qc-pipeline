import numpy as np
import nibabel as nib

def fit_first_level_glm(img, design_matrix):
    # Run voxel-wise Ordinary Least Squares (OLS) regression.
    data = img.get_fdata()
    shape = data.shape
    flat_data = data.reshape(-1, shape[3])
    
    X = design_matrix
    X_pinv = np.linalg.pinv(X)
    
    betas = np.dot(flat_data, X_pinv.T)
    beta_maps = betas.reshape(shape[0], shape[1], shape[2], X.shape[1])
    
    return beta_maps