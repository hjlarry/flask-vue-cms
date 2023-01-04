from apiflask import APIFlask, Schema, abort, HTTPTokenAuth, APIBlueprint, PaginationSchema, pagination_builder
from apiflask.fields import Integer, String, List, Nested, Field
from apiflask.validators import Length, OneOf, Range
from flask import current_app, request

from config import DevConfig
from models import User, Role
from ext import db
from utils import generate_token, auth_cache, verify_token

app = APIFlask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')
auth.verify_token(verify_token)
app.config.from_object(DevConfig)
db.init_app(app)

admin_bp = APIBlueprint('admin', __name__, url_prefix='/admin')

class BaseResponse(Schema):
    data = Field() 
    code = Integer(default=0)

app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse
app.config['BASE_RESPONSE_DATA_KEY '] = 'data'

@app.before_first_request
def create_tables():
    db.create_all()

    user = User.query.first()
    if user:
        return

    user1 = User(username='John',password="123", name='John Doe')
    user2 = User(username='admin',password="123", name='Admin Doe')
    role = Role(name='超级管理员', can_edit=False)
    user1.roles.append(role)
    user2.roles.append(role)
    db.session.add_all([user1, user2, role])

    db.session.commit()

@app.get('/')
def say_hello():
    return {'message': 'Hello!'}

class LoginScheme(Schema):
    username = String(required=True, validate=Length(min=3, max=40))
    password = String(required=True, validate=Length(min=3, max=40))

@admin_bp.post('/login')
@app.input(LoginScheme)
def login(data):
    user = User.query.filter_by(username=data['username']).first()
    if user and user.verify_password(data["password"]):
        token = generate_token(user.id).decode()
        res = {"data": {"token": token},"code":0}
        auth_cache.setex(user.id, current_app.config["EXPIRE_TIME"], token)
        return res
    return {'error': '用户名或密码错误', "code":1234}

class RoleScheme(Schema):
    id = Integer()
    name = String()
    can_edit = Integer()

class UserInfoScheme(Schema):
    id = Integer()
    username = String()
    name = String()
    avatar = String()
    roles = List(Nested(nested=RoleScheme))

@admin_bp.get('/info')
@app.output(schema=UserInfoScheme)
@app.auth_required(auth)
def get_info():
    return {"data":auth.current_user}

@admin_bp.get("/user/feature")
def get_feature():
    data = [
        {
            "title": "Vue3 + 全家桶",
            "percentage": 100,
            "content": '项目基于最新的<a target="_blank" href="https://v3.cn.vuejs.org/guide/introduction.html">vue3</a>全家桶进行开发，全面使用最新的的<a target="_blank" href="https://github.com/vuejs/rfcs/blob/master/active-rfcs/0040-script-setup.md">RFC script setup</a>语法标准，为你带来不一样的 vue3 开发体验',
        },
        {
            "title": "Element-Plus",
            "percentage": 100,
            "content": '<a target="_blank" href="https://element-plus.org/#/zh-CN">Element Plus</a>，一套为开发者、设计师和产品经理准备的基于 Vue 3.0 的桌面端组件库。是 Element UI 的官方 vue 3 兼容版本',
        },
    ]
    if request.headers.get("Accept-Language") == "en":
        data = [
            {
                "title": "Vue3 + whole",
                "percentage": 100,
                "content": "some thing",
            },
            {
                "title": "Element-Plus",
                "percentage": 100,
                "content": '<a target="_blank" href="https://element-plus.org/#/zh-CN">Element Plus</a>，Other thing',
            },
        ]
    return {"data": data, "code": 0}


@admin_bp.get("/user/chapter")
def get_chapter():
    data = [
        {"content": "课程导读", "timestamp": "第一章", "id": 1},
        {"content": " 标准化大厂编程规范解决方案之ESLint + Git Hooks ", "timestamp": "第二章", "id": 2},
        {"content": "项目架构解决方案之搭建登录基础架构", "timestamp": "第三章", "id": 3},
        {"content": "项目架构解决方案之搭建Layout基础架构", "timestamp": "第四章", "id": 4},
    ]
    return {"data": data, "code": 0}

class UserListQuery(Schema):
    page = Integer(load_default=1)
    per_page = Integer(load_default=20, validate=Range(min=1, max=30))

class UsersOut(Schema):
    users = List(Nested(nested=UserInfoScheme))
    pagination = Nested(nested=PaginationSchema)

@admin_bp.get("/user/list")
@app.input(UserListQuery, location="query")
@app.output(schema=UsersOut)
def get_userlist(params):
    paganition = User.query.paginate(page=params['page'], per_page=params['per_page'])
    return_data = {"users": paganition.items, "pagination": pagination_builder(paganition)}   
    return {"data":return_data}

app.register_blueprint(blueprint=admin_bp)