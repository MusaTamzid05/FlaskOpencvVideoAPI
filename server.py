from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
import werkzeug

from window import Window
import numpy as np
import cv2
import threading

parser = reqparse.RequestParser()
parser.add_argument("file", type = werkzeug.datastructures.FileStorage, location = "files")
parser.add_argument("width", type = str, help = "width of the image")
parser.add_argument("height", type = str, help = "height of the image")
parser.add_argument("channel", type = str, help = "channels of the image")



app = Flask(__name__)
api = Api(app)
window = Window(window_name = "test")

src_image = None

class Server(Resource):

    def post(self):

        global src_image
        req_parser = parser.parse_args()
        self._load_image(req_parser["file"])
        return {"test" : "q"}

    def _load_image(self, req_data):

        global src_image

        image_data = req_data.read()
        np_image = np.fromstring(image_data, np.uint8)
        src_image = cv2.imdecode(np_image, cv2.IMREAD_UNCHANGED)



api.add_resource(Server, "/")



def run_video():
    while True:
        current_image = src_image
        print(src_image)

        if current_image is not None:
            cv2.imshow("test", current_image)
            cv2.waitKey(1)




if __name__ == "__main__":
    threading.Thread(target = app.run, args = ("0.0.0.0", 5000) ).start()
    threading.Thread(target = run_video).start()



