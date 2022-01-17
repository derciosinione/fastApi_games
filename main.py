from unicodedata import name
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self, name):
        return {"name": name}


api.add_resource(HelloWorld, '/helloworld/<string:name>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
    
    
    
    
    
# @app.route('/', methods=['GET', 'POST'])
# def welcome():
#     return 'hello flask, i am back'

# @app.route('/games', methods=['GET', 'POST'])
# def games():
#     response = {'id': 1, 'name': 'Roleta Russa'};
#     return jsonify(response)
