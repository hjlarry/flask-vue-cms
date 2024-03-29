from apiflask import Schema, PaginationSchema
from apiflask.fields import Integer, String, List, Nested, Field, Dict, DateTime
from apiflask.validators import Length, Range


class BaseResponse(Schema):
    data = Field()
    code = Integer(default=0)


http_error_schema = {
    "properties": {
        "error_detail": {"type": "object"},
        "error_message": {"type": "string"},
        "code": {"type": "integer"},
    },
    "type": "object",
}


class RoleSchema(Schema):
    id = Integer()
    title = String()
    description = String()


class LoginSchema(Schema):
    username = String(required=True, validate=Length(min=3, max=40))
    password = String(required=True, validate=Length(min=3, max=40))


class UserInfoSchema(Schema):
    id = Integer()
    username = String()
    name = String()
    avatar = String()
    roles = List(Nested(nested=RoleSchema))
    permissions = Dict()
    created_at = DateTime(data_key="openTime")


class UserDetailSchema(UserInfoSchema):
    remark = List(String())
    experience = List(Dict())
    gender = String()
    mobile = String()
    province = String()
    nationality = String()
    address = String()
    major = String()
    glory = String()


class ListQuery(Schema):
    page = Integer(load_default=1)
    per_page = Integer(load_default=20, validate=Range(min=1, max=30))


class UsersOut(Schema):
    users = List(Nested(nested=UserInfoSchema))
    pagination = Nested(nested=PaginationSchema)


class ImportUser(Schema):
    users = Field()


class PermissionSchema(Schema):
    permission_id = String(data_key="id")
    permission_name = String()
    permission_mark = String()
    permission_desc = String()
    children = List(Nested(nested="self"))


class SetPermissionIn(Schema):
    permissions = List(String())


class ArticleSchema(Schema):
    id = Integer()
    title = String()
    description = String(data_key="desc")
    author = String()
    content = String()
    created_at = DateTime(data_key="publicDate")


class ArticlesOut(Schema):
    articles = List(Nested(nested=ArticleSchema))
    pagination = Nested(nested=PaginationSchema)


class ArticleIn(Schema):
    title = String()
    content = String()
