import cv2
import numpy as np

class Window:

    def __init__(self, window_name):
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        pass



    def show(self, req_data):
        image_data = req_data.read()
        np_image = np.fromstring(image_data, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_UNCHANGED)
        print(image.shape)

