from views import *
from app import myapp,api # importing myapp registers the url idk for some reason

api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(AddToDo, '/addtodo')


# api.add_resource(Home, '/')
# api.add_resource(Login, '/login')
# api.add_resource(SignUp, '/signup')
# api.add_resource(Users, '/users')
# api.add_resource(ToDos, '/todo')
# api.add_resource(Tasks, '/alltasks')
# api.add_resource(MyTasks, '/tasks')
# api.add_resource(EditTask, '/edit_task/<int:id>')
# api.add_resource(DeleteTask, '/delete_task/<int:id>')