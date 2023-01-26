from models.base_model import BaseQueries, BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class UserMethods(BaseQueries):
    model = User
