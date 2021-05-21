import cv2
from cv2 import CascadeClassifier
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle

class Face(object):
    def __init__(self, image, config):
        self.pixels = imread(image)
        self.cascade = CascadeClassifier(config)
    def showBoxes(self, cc,sc):
        bboxes = self.cascade.detectMultiScale(self.pixels, cc, sc)

        # print bounding box for each detected face
        for box in bboxes:
            # extract
            x, y, width, height = box
            x2, y2 = x + width, y + height
            # draw a rectangle over the pixels
            rectangle(self.pixels, (x, y), (x2, y2), (0,0,255), 1)

            imshow('Face detection', self.pixels)
