from pickle import TRUE
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)

Videos = {1: "deerone", 2: "dercio"}


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video is required.', required=True)
video_put_args.add_argument('viwes', type=int, help='Viwes of the video is required.', required=True)
video_put_args.add_argument('likes', type=int, help='Likes of the video is required.', required=True)

class Video(Resource):
    def get(self, id):
        print(request.method)
        return Videos[id]
    
    def put(self, id):
        args = video_put_args.parse_args()
        Videos[id] = args
        return Videos[id], 200


api.add_resource(Video, '/videos/<int:id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
    
    
    
    
    

