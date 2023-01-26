from flask_apispec import marshal_with, use_kwargs
from typing import Dict
from db import db
from flask_restful import Resource
from todo.controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task,
    delete_task_by_id
)
from todo.schema import (
    TaskGetRequestSchema, TaskGetResponseSchema,
    TaskPostRequestSchema, TaskUpdateRequestSchema,
    TaskDeleteRequestSchema, TaskDeleteResponseSchema
)


class TodoTasks(Resource):
    # @jwt_required
    @use_kwargs(TaskGetRequestSchema, locations=['json'])
    @marshal_with(TaskGetResponseSchema, 200)
    def get(self, task_id: int = None):
        if task_id:
            return get_task_by_id(task_id)
        return get_all_tasks()

    # @jwt_required
    @use_kwargs(TaskPostRequestSchema, locations=['json'])
    @marshal_with(TaskGetResponseSchema, 200)
    def post(self, **kwargs: Dict) -> Dict:
        resp = create_task(data={})
        db.commit()
        return resp

    # @jwt_required
    @use_kwargs(TaskUpdateRequestSchema, locations=['json'])
    @marshal_with(TaskGetResponseSchema, 200)
    def put(self, task_id: int, **kwargs: Dict) -> Dict:
        content = kwargs.get('content')
        resp = update_task(task_id, content)
        db.commit()
        return resp

    # @jwt_required
    @use_kwargs(TaskDeleteRequestSchema, locations=['json'])
    @marshal_with(TaskDeleteResponseSchema, 200)
    def delete(self, task_id: int) -> Dict:
        resp = delete_task_by_id(task_id)
        db.commit()
        return {"success": resp}
