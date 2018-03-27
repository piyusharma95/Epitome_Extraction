import nibabel as nib
import matplotlib.pyplot as plt
from nipype.interfaces import fsl
from nipype import Node, Workflow
import os
import fnmatch


def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, 4)       # changes as per the length of slice
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")


file_path = "/Users/doxbin/Desktop/SMH/benign/"

count=0
# input_file = file_path+'BRAINIX_NIFTI_T1.nii'
for input_file in os.listdir(file_path):
	if fnmatch.fnmatch(input_file, "LGG*"):
		print input_file
		file_in = file_path + input_file
		img = nib.load(file_in)
		img_data = img.get_data()
		shape = img_data.shape # shape of 3D matrix

		#for printing the Images
		# slice_list=[]
		# for i in [1,7,14,21]:               #for different parts scanned during MRI 
		# 	slice_list.append(img_data[:, :, i])         # making a 3D matrix

		# show_slices(slice_list)
		# plt.suptitle("Original NIfTI Images")
		# plt.show()	

		#Skull Stripping
		output_strip_file = "skull_stripping_"+input_file
		# skullstrip = Node(fsl.BET(in_file=file_in, mask=True), name="skullstrip")
		skullstrip = fsl.BET(in_file=file_path+input_file, out_file=file_path+output_strip_file,mask=True)
		skullstrip.run()

		# Inhomogeneity Correction(Smoothing)
		output_smooth_file = "smooth_"+input_file
		# smooth = Node(fsl.IsotropicSmooth(in_file=file_in, fwhm=4), name="smooth")
		smooth = fsl.IsotropicSmooth(in_file=file_path+output_strip_file, out_file=file_path+"/../output/benign/"+output_smooth_file,fwhm=4)
		smooth.run()

		# Mask process
		# mask = Node(fsl.ApplyMask(), name="mask")

		# Initiation of a workflow
		# wf = Workflow(name="smoothflow", base_dir=file_path+"output/")

		# First the "simple", but more restricted method
		# wf.connect(skullstrip, "mask_file", mask, "mask_file")

		# Now the more complicated method
		# wf.connect([(smooth, mask, [("out_file", "in_file")])])
		# wf.run()
		print count
		count = count + 1
		# wf.write_graph("workflow_graph.dot")
		# from IPython.display import Image
		# Image(filename=file_path+"output/smoothflow/workflow_graph.png")




		# img = nib.load(file_path+input_file)
		# img_data = img.get_data()
		# slice_list=[]
		# for i in [1,7,14,21]:               #for different parts scanned during MRI 
		# 	slice_list.append(img_data[:, :, i])         # making a 3D matrix

		# show_slices(slice_list)
		# plt.suptitle("Resultant NIfTI Images")
		# plt.show()






