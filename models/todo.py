from sqlalchemy.orm import relationship
from models.base_model import BaseQueries, BaseModel
from sqlalchemy import Column, ForeignKey, String, Boolean
from models.user import User


class ToDo(BaseModel):
    user = relationship(User, backref="todos")
    user_id = Column(None, ForeignKey(User.id, ondelete="CASCADE"))
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)


class ToDoMethods(BaseQueries):
    model = ToDo
