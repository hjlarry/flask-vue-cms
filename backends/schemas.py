from apiflask import Schema, PaginationSchema
from apiflask.fields import Integer, String, List, Nested, Field, DateTime
from apiflask.validators import Length, Range
from apiflask.schemas import validation_error_detail_schema


class BaseResponse(Schema):
    data = Field()
    code = Integer(default=0)


class RoleScheme(Schema):
    id = Integer()
    name = String()
    can_edit = Integer()


class LoginScheme(Schema):
    username = String(required=True, validate=Length(min=3, max=40))
    password = String(required=True, validate=Length(min=3, max=40))


class UserInfoScheme(Schema):
    id = Integer()
    username = String()
    name = String()
    avatar = String()
    roles = List(Nested(nested=RoleScheme))
    created_at = DateTime(data_key="openTime")


class UserListQuery(Schema):
    page = Integer(load_default=1)
    per_page = Integer(load_default=20, validate=Range(min=1, max=30))


class UsersOut(Schema):
    users = List(Nested(nested=UserInfoScheme))
    pagination = Nested(nested=PaginationSchema)

http_error_schema = {
    "properties": {
        "error_detail": {
            "type": "object"
        },
        "error_message": {
            "type": "string"
        },
        "code": {
            "type": "integer"
        }
    },
    "type": "object"
}

