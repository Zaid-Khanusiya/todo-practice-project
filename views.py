import random
from flask import request
from models import *
from flask_restful import Resource
from utils import *

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not all([name, email, password]):
            return {'errors': ['Name, email, and password are required.']}, 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'errors': ['User with this email already exists.']}, 400
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return "Your Sign-Up is successful"
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        verify_user = User.query.filter_by(email=email).first()
        if not verify_user:
            return {'error':'User not found!'}
        if verify_user.email == email and verify_user.password == password:
            token_check = Token.query.filter_by(email=email).first()
            token = str(random.randint(1111111111,9999999999))
            if token_check:
                token_check.token = token
                db.session.commit()
                return {"email": email, "token": token}
            else:
                new_token = Token(email=email, token=token)
                db.session.add(new_token)
                db.session.commit()
                return {"email": email, "token": token}
        else:
            return "User or pasword is invalid", 400
        
class AddToDo(Resource):
    @user_auth
    def post(self,email):
        data = request.get_json()
        task = data.get('task')
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'error':'User Not Found!'}
        new_task = ToDo(user_id=user.user_id, task=task)
        db.session.add(new_task)
        db.session.commit()
        return "Your task is added succcessfully!"