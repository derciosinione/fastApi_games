from flask import Flask
from flask_restful import Api, Resource, abort, reqparse


app = Flask(__name__)
api = Api(app)

Videos = {1: "derone", 2: "dercio"}


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video is required.', required=True)
video_put_args.add_argument('viwes', type=int, help='Viwes of the video is required.', required=True)
video_put_args.add_argument('likes', type=int, help='Likes of the video is required.', required=True)

class Video(Resource):
    def get(self, id):
        abort_if_video_id_doesent_exist(id)
        return Videos[id]
    
    def put(self, id):
        abort_if_video_id_doesent_exist(id)
        args = video_put_args.parse_args()
        Videos[id] = args
        return Videos[id], 200


def abort_if_video_id_doesent_exist(id):
    if id not in Videos:
        abort(404,  message="Video id is not valid...")
        

api.add_resource(Video, '/videos/<int:id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
    
    
    
    
    

