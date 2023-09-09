# Converting_Nifti_to_2D_jpeg_file
Converts Nifti files to jpeg or png file

The function nifti2image converts nifti file to jpeg/png series.
To use, 3 parameters are required.

in_path: path to nifti file

num_slices: number of slices in the scan. This can be checked using medical imaging softwares like 3dslicer or ITKsnap

out_path: path to output.

Nifti will be saved as jpeg file as default. If you wish to save it as png file format, just simply put png=True as your fourth parameter.

Example result:
<p align="center">
  <img src="https://github.com/KWKIM128/3D-UNet/assets/115262940/e8c06659-2df5-40c6-b595-11549e97e509" />
</p>
