from typing import Dict, List

from sqlalchemy.orm import Session
from werkzeug.exceptions import BadRequest

from common.constants import TASK_NOT_FOUND
from models.todo import TaskMethods, Task


def create_task(db: Session, data: Dict) -> Dict:
    """
    Create a task
    """
    task = TaskMethods.create_record(values=data, db=db)
    return task


def get_all_tasks(db: Session, current_user: int) -> Dict[str, List]:
    """
    Get all tasks
    """
    tasks = TaskMethods.get_all_record_with_(db, user_id=current_user)
    if not tasks:
        raise BadRequest(TASK_NOT_FOUND)
    return {"tasks": tasks}


def get_task_by_id(db: Session, task_id: int, current_user: int) -> Dict[str, List]:
    """
    Get a task by task_id
    """
    task = TaskMethods.get_record_with_(db, id=task_id, user_id=current_user)
    if not task:
        raise BadRequest(TASK_NOT_FOUND)
    return {"tasks": [task]}


def update_task(
    db: Session, task_id: int, description: str, current_user: int, completed: bool
) -> Task:
    """
    Update task by task_id
    """
    task = TaskMethods.get_record_with_(db, id=task_id, user_id=current_user)
    if not task:
        raise BadRequest(TASK_NOT_FOUND)
    task.description = description if description else task.description
    task.completed = completed if completed else task.completed
    return task


def delete_task_by_id(db: Session, task_id: int, current_user: int) -> bool:
    """
    Delete a task by task_id
    """
    task = TaskMethods.get_record_with_(db, id=task_id, user_id=current_user)
    if not task:
        raise BadRequest(TASK_NOT_FOUND)
    db.delete(task)
    return True
