from marshmallow import fields, Schema


class TaskGetRequestSchema(Schema):
    task_id = fields.Int()


class TasksGetSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String()
    completed = fields.Boolean()


class TaskGetResponseSchema(Schema):
    tasks = fields.List(fields.Nested(TasksGetSchema), many=True, dump_default=[])

    class Meta:
        strict = True


class TaskPostRequestSchema(Schema):
    title = fields.String(required=True)
    description = fields.String()


class TaskUpdateRequestSchema(Schema):
    task_id = fields.Int(required=True)
    description = fields.String()
    completed = fields.Boolean()


class TaskDeleteRequestSchema(Schema):
    task_id = fields.Int(required=True)


class TaskDeleteResponseSchema(Schema):
    success = fields.Boolean(required=True)
