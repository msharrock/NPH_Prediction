
import numpy as np
import os
import CTtools
import nibabel as nib
from subprocess import call
import sys
import ipdb

ct_scan_path = str(sys.argv[1])
if 'Ashu' in ct_scan_path:
	BASE = 'Ashu_Files'
else:
	BASE = ''
MNI_152 = os.path.join(os.getcwd(),'MNI152_T1_1mm.nii.gz')
nameOfAffineMatrix = ct_scan_path[:ct_scan_path.find('.nii.gz')]+'_affine.mat'
nameOfInvMatrix = ct_scan_path[:ct_scan_path.find('.nii.gz')]+'_inverse.mat'
ct_scan_wodevice = ct_scan_path

subject_name = os.path.split(ct_scan_path)[-1]
subject_name = subject_name[:subject_name.find('.nii.gz')]

segmentedMNI = os.path.join(BASE,'Final_Predictions', subject_name+'_MNI152.segmented1.nii.gz')
segmentedORIG = os.path.join(BASE,'Transformed_Predictions', subject_name+'.segmented.nii.gz')
orig_name = os.path.join(BASE,'Scans', subject_name+'.nii.gz')

try:

	call(['convert_xfm', '-omat', nameOfInvMatrix, '-inverse', nameOfAffineMatrix])
	
	call(['flirt','-in', segmentedMNI, '-ref', orig_name, '-applyxfm', '-init', nameOfInvMatrix, '-out', segmentedORIG, '-interp', 'nearestneighbour'])


except:
	print 'something did not work'

