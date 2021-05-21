import cv2
from cv2 import CascadeClassifier
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle

#get the image
pixels = imread('test2.jpg')

# load the cascade file
cascade = CascadeClassifier('haarcascade_frontalface_default.xml')

# perform face detection
bboxes = cascade.detectMultiScale(pixels, 1.05, 13)

# print bounding box for each detected face
for box in bboxes:
	# extract
	x, y, width, height = box
	x2, y2 = x + width, y + height
	# draw a rectangle over the pixels
	rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)

# show the image
imshow('Face detection', pixels)
waitKey(0)
destroyAllWindows()