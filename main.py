from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

Videos = {}

class HelloWorld(Resource):
    def get(self, name):
        return {"name": name}

class Video(Resource):
    def get(self, video_id):
        return Videos[video_id]
    
    def put(self, video_id):
        app.logger.info(request.form['likes'])
        app.logger.info(request.method['Post'])
        return Videos[video_id]


# api.add_resource(Video, '/video/')
api.add_resource(Video, '/video/<int:id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
    
    
    
    
    

