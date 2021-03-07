import cv2
import numpy as np

class Window:

    def __init__(self, window_name):
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        pass


    def show(self, req):
        current_image = req["file"]
        image = np.asarray(bytearray(current_image.read()), dtype = "uint8")
        print(image.shape)

