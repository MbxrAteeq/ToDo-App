from flask_apispec import marshal_with, use_kwargs
from typing import Dict
from db import db
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from todo.controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task,
    delete_task_by_id
)
from todo.schema import (
    TaskGetRequestSchema, TaskGetResponseSchema,
    TaskPostRequestSchema, TaskUpdateRequestSchema,
    TaskDeleteRequestSchema, TaskDeleteResponseSchema, TasksGetSchema
)


class TodoTasks(Resource):
    @jwt_required()
    @use_kwargs(TaskGetRequestSchema, locations=['json'])
    @marshal_with(TaskGetResponseSchema, 200)
    def get(self, task_id: int = None):
        current_user = get_jwt_identity()
        if task_id:
            return get_task_by_id(db, task_id, current_user)
        return get_all_tasks(db, current_user)

    @jwt_required()
    @use_kwargs(TaskPostRequestSchema, locations=['json'])
    @marshal_with(TasksGetSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        current_user = get_jwt_identity()
        task_data = {
            "title": kwargs.get("title"),
            "description": kwargs.get("description"),
            "user_id": current_user
        }
        resp = create_task(db=db, data=task_data)
        db.commit()
        return resp

    @jwt_required()
    @use_kwargs(TaskUpdateRequestSchema, locations=['json'])
    @marshal_with(TasksGetSchema, 200)
    def put(self, task_id: int, **kwargs: Dict) -> Dict:
        current_user = get_jwt_identity()
        description = kwargs.get('description')
        completed = kwargs.get('completed')
        resp = update_task(db, task_id, description, current_user, completed)
        db.commit()
        return resp

    @jwt_required()
    @use_kwargs(TaskDeleteRequestSchema, locations=['json'])
    @marshal_with(TaskDeleteResponseSchema, 200)
    def delete(self, task_id: int) -> Dict:
        current_user = get_jwt_identity()
        resp = delete_task_by_id(db, task_id, current_user)
        db.commit()
        return {"success": resp}
