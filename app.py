from flask import Flask
from flask_restful import Api

myapp = Flask(__name__)
api = Api(myapp)

from routes import *

# Run the app on localhost 5000 port
if __name__ == '__main__':
    myapp.run(port=5000, debug=True)