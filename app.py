from datetime import timedelta

from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from common.methods import encrypt_json_with_common_cipher
from todo.views import TodoTasks
from user.views import UserSignUp, UserLogin, DecryptData

env = Env()
env.read_env()


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
    hours=int(env("JWT_ACCESS_TOKEN_EXPIRES"))
)
jwt = JWTManager(app)


@app.after_request
def after_request(response):
    data = response.get_json()
    if not data.get('decrypted_data') and response.status_code == 200:
        response.data = encrypt_json_with_common_cipher(response.get_json())
    return response


@app.errorhandler(422)
def handle_unprocessable_entity(err):
    messages = err.exc.messages if err.exc else ["Invalid request"]
    return {"status": "error", "result": messages}, 422


api.add_resource(TodoTasks, "/todo")
api.add_resource(UserSignUp, "/signup")
api.add_resource(UserLogin, "/login")
api.add_resource(DecryptData, "/decrypt_data")

if __name__ == "__main__":
    app.run(debug=True)
