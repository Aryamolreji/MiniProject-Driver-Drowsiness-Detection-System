#Importing OpenCV Library for basic image processing functions
import cv2
# Numpy for array related functions
import numpy as np
# Dlib for deep learning based Modules and face landmark detection
import dlib
#face_utils for basic operations of conversion
from imutils import face_utils
#checking
#Initializing the camera and taking the instance
cap = cv2.VideoCapture(0)
#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#status marking for current state
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)
def compute(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist
def blinked(a,b,c,d,e,f):
	up = compute(b,d) + compute(c,e)
	down = compute(a,f)
	ratio = up/(2.0*down)
#Checking if it is blinked
	if(ratio>0.25):
		return 2
	elif(ratio>0.21 and ratio<=0.25):
		return 1
	else:
		return 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
#push

