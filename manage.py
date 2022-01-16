from crypt import methods
from unicodedata import name
from flask import Flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return 'hello flask, i am back'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)