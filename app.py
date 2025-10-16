from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
# import os

load_dotenv()

# SUPABASE_DB_URI = os.getenv("SUPABASE_DB_URI")
# print(SUPABASE_DB_URI)

myapp = Flask(__name__)
api = Api(myapp)

from routes import *

if __name__ == '__main__':
    myapp.run(port=6262, debug=True, host='0.0.0.0')