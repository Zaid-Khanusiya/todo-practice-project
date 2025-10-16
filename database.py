import os
from flask_sqlalchemy import SQLAlchemy
from app import myapp

db = SQLAlchemy()
SUPABASE_DB_URI = os.getenv("SUPABASE_DB_URI")
# print(SUPABASE_DB_URI)

# online supabase database linking connection
myapp.config['SQLALCHEMY_DATABASE_URI'] = SUPABASE_DB_URI

# myapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zaid:0000@localhost/todo'
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(myapp)