from flask_apispec import doc, marshal_with, use_kwargs
from typing import Dict
from db import db
from flask_restful import Resource
from user.controller import create_user, create_token


class UserSignUp(Resource):
    # @use_kwargs(UserRegisterRequestSchema, locations=['json'])
    # @marshal_with(UserRegisterResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        resp = create_user(data={})
        db.commit()
        return resp


class UserLogin(Resource):
    # @use_kwargs(UserLoginRequestSchema, locations=['json'])
    # @marshal_with(UserLoginResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        resp = create_token(data={})
        db.commit()
        return resp
