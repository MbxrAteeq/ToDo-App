from flask import Flask
from flask_restful import Api
from todo.views import TodoTasks
from user.views import UserSignUp, UserLogin

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoTasks, '/todo/<string:todo_id>')
api.add_resource(UserSignUp, '/signup/<string:todo_id>')
api.add_resource(UserLogin, '/login/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
