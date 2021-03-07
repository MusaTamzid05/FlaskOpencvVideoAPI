from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
import werkzeug

from window import Window

parser = reqparse.RequestParser()
parser.add_argument("file", type = werkzeug.datastructures.FileStorage, location = "files")
parser.add_argument("width", type = str, help = "width of the image")
parser.add_argument("height", type = str, help = "height of the image")
parser.add_argument("channel", type = str, help = "channels of the image")



app = Flask(__name__)
api = Api(app)
window = Window(window_name = "test")

class Server(Resource):

    def post(self):
        req_parser = parser.parse_args()
        window.show(req_parser["file"])
        return {"test" : "q"}


api.add_resource(Server, "/")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)



