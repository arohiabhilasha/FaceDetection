import cv2
from cv2 import CascadeClassifier
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from objects import Face

x = Face("imx.jpg", "haarcascade_frontalface_default.xml")
x.renderFaces(1.05,13)
x.destroyRender()