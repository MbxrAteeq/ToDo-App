from models.base_model import BaseQueries, BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = 'user'
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class UserMethods(BaseQueries):
    model = User
