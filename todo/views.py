from flask_apispec import doc, marshal_with, use_kwargs
from typing import Dict
from db import db
from flask_restful import Resource
from todo.controller import create_task, get_all_tasks, get_task_by_id, update_task, delete_task_by_id


class TodoTasks(Resource):
    # @jwt_required
    # @use_kwargs(TaskGetRequestSchema, locations=['json'])
    # @marshal_with(TaskPostResponseSchema, 200)
    def get(self, todo_id: int = None):
        if todo_id:
            return get_task_by_id(todo_id)
        return get_all_tasks()

    # @jwt_required
    # @use_kwargs(TaskPostRequestSchema, locations=['json'])
    # @marshal_with(TaskPostResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        resp = create_task(data={})
        db.commit()
        return resp

    # @jwt_required
    # @use_kwargs(TaskUpdateRequestSchema, locations=['json'])
    # @marshal_with(TaskUpdateResponseSchema, 200)
    def put(self, todo_id: int, **kwargs: Dict) -> Dict:
        content = kwargs.get('content')
        resp = update_task(todo_id, content)
        db.commit()
        return resp

    # @jwt_required
    # @use_kwargs(TaskDeleteRequestSchema, locations=['json'])
    # @marshal_with(TaskDeleteResponseSchema, 200)
    def delete(self, todo_id: int) -> bool:
        resp = delete_task_by_id(todo_id)
        db.commit()
        return resp
