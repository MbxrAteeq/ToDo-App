from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from models.base_model import BaseQueries, BaseModel
from models.user import User


class Task(BaseModel):
    __tablename__ = "task"
    user = relationship(User, backref="tasks")
    user_id = Column(None, ForeignKey(User.id, ondelete="CASCADE"))
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)


class TaskMethods(BaseQueries):
    model = Task
