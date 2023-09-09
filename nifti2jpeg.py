import numpy as np
import nibabel as nib
import os
from PIL import Image
from tqdm import tqdm

def nifti2jpeg(in_path, num_slices, out_path):
    """
    This function converts one nifti to jpeg series
    
    Input Parameter:
        in_path: path to nifti file
        nun_slices: number of slices in the scan
        out_path: path to output
    """

    nifti_name = os.path.basename(in_path).split(".")[0] # gets name of the nifti file
    
    nifti = nib.load(in_path).get_fdata() # reads/load nifti file
    new_image = nifti.astype(float)
    scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0 # rescaling the image
    nifti_arr = np.uint8(scaled_image)

    
    for i in tqdm(range(num_slices)):
        name = nifti_name + '_' + str(i)
        image = Image.fromarray(nifti_arr[:,:,i])
    
        image.save(out_path + '/' + name + '.jpeg')
