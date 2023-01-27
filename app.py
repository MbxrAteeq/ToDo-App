from flask import Flask
from flask_restful import Api
from todo.views import TodoTasks
from user.views import UserSignUp, UserLogin
from flask_jwt_extended import JWTManager
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=int(env("JWT_ACCESS_TOKEN_EXPIRES")))
jwt = JWTManager(app)


@app.errorhandler(422)
def handle_unprocessable_entity(err):
    messages = err.exc.messages if err.exc else ['Invalid request']
    return {'status': 'error', 'result': messages}, 422


api.add_resource(TodoTasks, '/todo')
api.add_resource(UserSignUp, '/signup')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    app.run(debug=True)
