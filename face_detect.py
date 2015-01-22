#!/usr/bin/env python

import cv2
import sys

# Get user supplied values
capture = cv2.VideoCapture(0)
#imagePath = sys.argv[1]
cascPath = sys.argv[1]
win1 = "Faces found"
cv2.namedWindow(win1)
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
while capture.isOpened():
	_, image = capture.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	#print "Found {0} faces!".format(len(faces))

	# Draw a rectangle around the faces
	#for (x, y, w, h) in faces:
	#	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow(win1, image)
	c = cv2.waitKey(1)
	if int(c)==27:
		break
capture.release()
cv2.destroyAllWindows()	
