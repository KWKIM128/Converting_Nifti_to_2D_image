# Converting_Nifti_to_2D_jpeg_file
Converts Nifti files to jpeg or png file

The function nifti2image converts nifti file to jpeg/png series. The binarymask_nifti2image function does the same thing as the nifti2image function but applies a binary threshold before converting it to 2D image.
To use, 3 parameters are required.

in_path: path to nifti file

num_slices: number of slices in the scan. This can be checked using medical imaging softwares like Slicer or ITKsnap

out_path: path to output.

Nifti will be saved as a jpeg file as default. If you wish to save it as a png file format, simply put png=True as your fourth parameter.

Example result:
<p align="center">
  <img src="https://github.com/KWKIM128/3D-UNet/assets/115262940/e8c06659-2df5-40c6-b595-11549e97e509" />
</p>
