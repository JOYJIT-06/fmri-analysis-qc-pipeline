import unittest
import os
import numpy as np
import nibabel as nib
from src.data_loader import validate_nifti_file, create_brain_mask

class TestDataLoader(unittest.TestCase):
    def test_invalid_extension(self):
        with self.assertRaises(ValueError):
            validate_nifti_file("test_file.txt")
            
    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            validate_nifti_file("nonexistent.nii.gz")
            
    def test_brain_mask_creation(self):
        data = np.zeros((10, 10, 10, 20))
        data[3:7, 3:7, 3:7, :] = 500.0
        img = nib.Nifti1Image(data, np.eye(4))
        mask = create_brain_mask(img)
        self.assertEqual(mask.shape, (10, 10, 10))
        self.assertEqual(mask.get_fdata()[5, 5, 5], 1)