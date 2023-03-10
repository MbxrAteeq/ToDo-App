from marshmallow import fields, Schema


class UserRegisterRequestSchema(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)


class UserRegisterResponseSchema(Schema):
    success = fields.Boolean(required=True)


class UserLoginRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class UserLoginResponseSchema(Schema):
    status = fields.String(required=True)
    access_token = fields.String(required=True)


class DecryptDataRequestSchema(Schema):
    decryption_key = fields.String(required=True)
    encrypted_data = fields.String(required=True)


class DecryptDataResponseSchema(Schema):
    decrypted_data = fields.Dict(required=True)
