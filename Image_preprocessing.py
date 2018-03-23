from nilearn.image import smooth_img
from nilearn.plotting import plot_anat
import nibabel as nib
import matplotlib.pyplot as plt

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, 4)       # changes as per the length of slice
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")


file_path = "/Volumes/Casimer/Neurohacking_data-0.0/Neurohacking_data-0.0/BRAINIX/NIfTI/"
# for file in os.listdir(file_path):
# 	if fnmatch.fnmatch(file, '*BRAINIX_NIFTI*'):
# 		print file

img = nib.load(file_path+'BRAINIX_NIFTI_FLAIR.nii.gz')
img_data = img.get_data()
shape = img_data.shape # shape of 3D matrix
# display = plot_anat(img, title="MRI scan")
# display.close()


slice_list=[]
for i in [1,7,14,21]:               #for different parts scanned during MRI 
	slice_list.append(img_data[:, :, i])         # making a 3D matrix

show_slices(slice_list)
plt.suptitle("NIfTI Images showing different parts") 
plt.show()	

# result_img = smooth_img(img_data, img.affine, fwhm=None, ensure_finite=True, copy=True)

