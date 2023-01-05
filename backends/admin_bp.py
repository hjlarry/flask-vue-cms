from apiflask import HTTPTokenAuth, APIBlueprint, pagination_builder
from flask import current_app, request

from utils import generate_token, auth_cache, verify_token
from schemas import LoginScheme, UserInfoScheme, UserListQuery, UsersOut, ImportUser
from ext import db
from models import User

admin_bp = APIBlueprint("admin", __name__, url_prefix="/admin")
auth = HTTPTokenAuth(scheme="Bearer")
auth.verify_token(verify_token)


@admin_bp.post("/login")
@admin_bp.input(LoginScheme)
def login(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.verify_password(data["password"]):
        token = generate_token(user.id).decode()
        res = {"data": {"token": token}, "code": 0}
        auth_cache.setex(user.id, current_app.config["EXPIRE_TIME"], token)
        return res
    return {"error": "用户名或密码错误", "code": 1234}


@admin_bp.get("/info")
@admin_bp.output(schema=UserInfoScheme)
@admin_bp.auth_required(auth)
def get_info():
    return {"data": auth.current_user}


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


@admin_bp.get("/user/list")
@admin_bp.input(UserListQuery, location="query")
@admin_bp.output(schema=UsersOut)
def get_userlist(params):
    paganition = User.query.paginate(page=params["page"], per_page=params["per_page"])
    return_data = {
        "users": paganition.items,
        "pagination": pagination_builder(paganition),
    }
    return {"data": return_data}


@admin_bp.post('/user/batchImport')
@admin_bp.input(ImportUser)
def import_users(data):
    try:
        for item in data['users']:
            user = User(name=item['name'], username=item['username'], password='123')
            db.session.add(user)
        db.session.commit()
    except:
        return {"code": 2000, "error": "some data import error!"}
    return {"code":0}

@admin_bp.post('/user/delete/<int:id>')
def delete_user(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"code": 2000, "error": "some data delete error!"}
    return {"code":0}