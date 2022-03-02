"""
@author: Muhammad Hanan Asghar
Script that resizes images
"""
import cv2
import glob

images = glob.glob("dataset/arham/*.jpg")
for image in images:
	filename = image.split("/")[-1]
	img = cv2.imread(image)
	res = cv2.resize(img, (96, 96))
	# imag = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
	cv2.imwrite(f"cropped/arham/{filename}", res)
	print(f"Saved: cropped/arham/{filename}")
