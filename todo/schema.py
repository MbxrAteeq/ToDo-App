from marshmallow import fields, Schema


class TaskGetRequestSchema(Schema):
    todo_id = fields.Int()


class TasksGetSchema(Schema):
    user_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String()
    completed = fields.String()


class TaskGetResponseSchema(Schema):
    tasks = fields.List(fields.Nested(TasksGetSchema))

    class Meta:
        strict = True


class TaskPostRequestSchema(Schema):
    title = fields.String(required=True)
    description = fields.String()
    completed = fields.String()


class TaskUpdateRequestSchema(Schema):
    description = fields.String()
    completed = fields.String()


class TaskDeleteRequestSchema(Schema):
    todo_id = fields.Int()


class TaskDeleteResponseSchema(Schema):
    success = fields.Boolean(required=True)

