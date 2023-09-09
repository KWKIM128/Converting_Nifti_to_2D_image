import numpy as np
import nibabel as nib
import os
from PIL import Image

def nifti2jpeg(in_path, num_slices, out_path):
    """
    Input Parameter:
        in_path: folder where nifti file is located
        nun_slices: number of slices in the scan
        out_path: folder where the jpeg will be saved
    """
    
    nifti = nib.load(in_path).get_fdata()
    nifti = nifti.astype(np.uint8)
    nifti_name = os.path.basename(in_path).split(".")[0]

    
    for i in range(num_slices):
        name = nifti_name + '_' + str(i)
        image = Image.fromarray(nifti[:,:,i])
    
        image.save(out_path + '/' + name + '.jpeg')
