from typing import Dict, List
from flask_sqlalchemy.session import Session

from common.constants import TASK_NOT_FOUND
from models.todo import TaskMethods


def create_task(db: Session, data: Dict) -> Dict:
    """
    Create a task
    """
    task = TaskMethods.create_record(values=data, db=db)
    return {"tasks": task}


def get_all_tasks(db: Session, current_user: int) -> List[Dict]:
    """
    Get all tasks
    """
    tasks = TaskMethods.get_all_record_with_(db, user_id=current_user)
    return tasks


def get_task_by_id(db: Session, task_id: int, current_user: int) -> Dict:
    """
    Get a task by task_id
    """
    task = TaskMethods.get_record_with_(
        db, id=task_id,
        user_id=current_user
    )
    return task


def update_task(db: Session, task_id: int, data: Dict, current_user: int) -> Dict:
    """
    Update task by task_id
    """
    task = TaskMethods.get_record_with_(
        db, id=task_id,
        user_id=current_user
    )
    if not task:
        raise Exception(TASK_NOT_FOUND)
    return {"tasks": {}}


def delete_task_by_id(db: Session, task_id: int, current_user: int) -> bool:
    """
    Get a task by task_id
    """
    return True
