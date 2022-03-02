"""
@author: Muhammad Hanan Asghar
"""

#!/usr/bin/env python
# coding: utf-8


# Libraries

import dlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
import uuid

# Detector Model(Face)
detector = dlib.get_frontal_face_detector()



# Main folder where all classes saved
main_folder = "dataset"

# Classes where to store faces its one or may be more than one
folders = ["Ehsan", "Mohsin", "Arham"]

# Checking if classes folders present in main folder if not then 
# make new folder
try:
    for folder in folders:
        path = os.path.join(os.getcwd(), main_folder, folder)
        if not os.path.exists(path):
            os.mkdir(path)
except:
    print("Error Occured")


def gen_faces(image):
    """
    Function that gets image as input and generate face from it and returns
    face from the image.
    """
    image_height, image_width, _ = image.shape
    faces = []
    detections = detector(image)
    for i, d in enumerate(detections):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))
        # Croping Face from image
        crop_img = image[max(0, d.top()): min(d.bottom(), image_height),
                    max(0, d.left()): min(d.right(), image_width)]
        faces.append(crop_img)
#     returning array of faces
    return faces



video = cv2.VideoCapture("/home/sultan/Desktop/JupyterNotebooks/dataset/mohsin.mp4")
while True:
    
    # Reading Frames
    ret, frame = video.read()
    if not ret:
        break
    # Generating Faces
    face = gen_faces(frame)[0]
    face = cv2.resize(face, (128, 128))
    
    frame = cv2.resize(frame, (64, 64))
    cv2.imshow("Video", frame)
    
    # Unique Filename
    filename = os.path.join(os.getcwd(), "dataset", "Mohsin", f"{uuid.uuid1()}.jpg")
    
    # Saving Face
    cv2.imwrite(filename, face)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()





