import cv2
from cv2 import CascadeClassifier
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle

class Atom(object):
    def __init__(self, name, symbol, valency):
        self.valency = valency
        self.name = name
        self.symbol = symbol
    
    def shell(self, electrons, ss, ps, ds, fs):
        if (ss+ps+ds+fs) > electrons:
            return False
        else:
            self.shell = {"electron":electrons,"s":ss,"p":ps, "d":ds, "f":fs}
            return self.shell

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

atom1 = Atom("Hydrogen", "H", 3)
print(atom1.name)
print(atom1.shell(6, 2, 4, 1, 0))
print(atom1.shell)