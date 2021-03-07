from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
import werkzeug

parser = reqparse.RequestParser()
parser.add_argument("file", type = werkzeug.datastructures.FileStorage, location = "files")


app = Flask(__name__)
api = Api(app)


class Server(Resource):

    def post(self):
        data = parser.parse_args()
        print(data)
        return {"test" : "q"}


api.add_resource(Server, "/")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)



