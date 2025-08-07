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
                return {"Your Email:": email, "Your Token:": token}
            else:
                new_token = Token(email=email, token=token)
                db.session.add(new_token)
                db.session.commit()
                return {"Your Email:": email, "Your Token:": token}
        else:
            return "User or pasword is invalid", 400
        
class AddToDo(Resource):
    @user_auth # this is a python decorator which will authenticate user with email & token...
    def post(self,email): # this email field will come from(return) the decorator function defined in utils.py
        data = request.get_json()
        task = data.get('task')
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'error':'User Not Found!'}
        new_task = ToDo(user_id=user.user_id, task=task)
        db.session.add(new_task)
        db.session.commit()
        return "Your task is added succcessfully!"
    
# this only lets view tasks to the users who are authenticated and are proven owners of tasks
class ViewToDo(Resource):
    @user_auth
    def post(self,email):
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'error':'User Not Found!'}, 400
        user_todos = ToDo.query.filter_by(user_id=user.user_id).all()
        result = []
        for item in user_todos:
            result.append(item.task)
        return {'Your Tasks:':result}

# this edit todo first authenticates by header token and then passes to route function
# and again this route function checks that does that task belong to that user only then allows to update
class EditToDo(Resource):
    @user_auth
    def post(self,email): 
        data = request.get_json()
        todo_id = data.get('task_id')
        updated_task = data.get('updated_task')
        task = ToDo.query.filter_by(todo_id=todo_id).first()
        if not task:
            return {'error':'Task Not Found!'},400
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'error':'User Not Found!'},400
        if user.user_id != task.user_id:
            return {'error':'The task is not registered under you!'},400
        task.task = updated_task
        db.session.commit()
        return "Your Task Has Been Updated Successfully!"