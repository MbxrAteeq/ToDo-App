from typing import Dict

from environs import Env
from flask_apispec import marshal_with, use_kwargs
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from common.constants import WRONG_CREDENTIALS, DECRYPTION_KEY_ERROR, NO_DATA_FOUND
from common.methods import hash_password, decrypt_json_with_common_cipher
from db import db
from user.controller import (
    create_user,
    create_token,
    check_user_already_exists,
    validate_user,
)
from user.schema import (
    UserRegisterRequestSchema,
    UserRegisterResponseSchema,
    UserLoginRequestSchema,
    UserLoginResponseSchema,
    DecryptDataRequestSchema,
    DecryptDataResponseSchema,
)

env = Env()
env.read_env()


class UserSignUp(Resource):
    @use_kwargs(UserRegisterRequestSchema, locations=["json"])
    @marshal_with(UserRegisterResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        password = hash_password(kwargs.get("password"))
        user = check_user_already_exists(db, kwargs.get("email"))
        if user:
            raise BadRequest(f"user with email: {kwargs.get('email')} already exists")
        user_data = {
            "name": kwargs.get("name"),
            "email": kwargs.get("email"),
            "password": password,
        }
        resp = create_user(db=db, data=user_data)
        db.commit()
        return {"success": resp}


class UserLogin(Resource):
    @use_kwargs(UserLoginRequestSchema, locations=["json"])
    @marshal_with(UserLoginResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        data = {"email": kwargs.get("email"), "password": kwargs.get("password")}
        logged_in_user = validate_user(db=db, data=data)
        if not logged_in_user:
            raise BadRequest(WRONG_CREDENTIALS)
        resp = create_token(user_data=logged_in_user)
        return resp


class DecryptData(Resource):
    @use_kwargs(DecryptDataRequestSchema, locations=["json"])
    @marshal_with(DecryptDataResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        if kwargs.get("decryption_key") != env("DECRYPTION_KEY"):
            raise BadRequest(DECRYPTION_KEY_ERROR)
        data = decrypt_json_with_common_cipher(kwargs.get("encrypted_data"))
        if not data:
            raise BadRequest(NO_DATA_FOUND)
        return {"decrypted_data": data}
