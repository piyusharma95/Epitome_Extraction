import xlrd
import os
import shutil


current_dir = os.getcwd()
path = current_dir + "/disease_list.xlsx"
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)

error_dir = []
for row in range(1,160):
	folder_name = first_sheet.cell(row,0).value
	grade = first_sheet.cell(row,2).value
	file_in = current_dir + "/NiFTiSegmentationsEdited/" + folder_name + "/"+folder_name+"_T2.nii.gz"

	if grade==2:
		file_out = current_dir + "/benign/"
	elif grade==3:
		file_out = current_dir + "/malignant/"
	
	try:
		shutil.copy(file_in, file_out)
	except:
		error_dir.append(file_in)
	print "row" + str(row)

print "Error Directory"
print error_dir