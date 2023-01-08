from apiflask import HTTPTokenAuth, APIBlueprint, pagination_builder
from flask import request

from utils import verify_token
from schemas import (
    UserInfoSchema,
    UserDetailSchema,
    UserListQuery,
    UsersOut,
    ImportUser,
    RoleSchema,
    PermissionSchema,
    SetPermissionIn,
)
from ext import db
from models import User, Role, Permission

admin_bp = APIBlueprint("admin", __name__, url_prefix="/admin")
auth = HTTPTokenAuth(scheme="Bearer")
auth.verify_token(verify_token)


@admin_bp.before_request
@admin_bp.auth_required(auth)
def whole_bp_need_login():
    pass


@admin_bp.get("/info")
@admin_bp.output(schema=UserInfoSchema)
def get_info():
    data = {
        "menus": [
            "userManage",
            "roleList",
        ],
        "points": [
            "distributeRole",
            "importUser",
        ]
    }

    auth.current_user.__dict__['permissions'] = data
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


@admin_bp.post("/user/batchImport")
@admin_bp.input(ImportUser)
def import_users(data):
    try:
        for item in data["users"]:
            user = User(name=item["name"], username=item["username"], password="123")
            db.session.add(user)
        db.session.commit()
    except:
        return {"code": 2000, "error": "some data import error!"}
    return {"code": 0}


@admin_bp.post("/user/delete/<int:id>")
def delete_user(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"code": 2000, "error": "some data delete error!"}
    return {"code": 0}


@admin_bp.get("/user/<int:id>")
@admin_bp.output(UserDetailSchema)
def get_user(id):
    user = User.query.get(id)
    data = {
        "remark": ["超级管理员", "BOSS"],
        "experience": [
            {
                "startTime": "2016-05-24",
                "endTime": "2017-05-24",
                "title": "慕课网",
                "desc": "混合开发京东商城",
            },
            {
                "startTime": "2018-06-01",
                "endTime": "2019-08-12",
                "title": "慕课网",
                "desc": "uni-app 开发企业级小程序",
            },
        ],
        "openTime": "2016-05-24",
        "mobile": "188xxxx0001",
        "avatar": "https://m.imooc.com/static/wap/static/common/img/logo-small@2x.png",
        "gender": "男",
        "province": "北京",
        "nationality": "汉",
        "address": "北京市朝阳区xx大道 11xx0 号 3 层",
        "major": "在线职业教育平台",
        "glory": "国内领先的线上 IT 教育品牌",
    }
    user.__dict__.update(data)
    return {"data": user}


@admin_bp.get("/user/role/<int:id>")
@admin_bp.output(RoleSchema(many=True))
def get_user_role(id):
    db_roles = User.query.get(id).roles
    return {"data": db_roles}


@admin_bp.post("/user/role/<int:id>")
@admin_bp.input(RoleSchema(many=True))
def update_user_role(id, data):
    user = User.query.get(id)
    roles = []
    for item in data:
        role = Role.query.get(item["id"])
        roles.append(role)
    user.roles = roles
    db.session.commit()
    return {"code": 0}


@admin_bp.get("/role/list")
@admin_bp.output(RoleSchema(many=True))
def roles():
    db_roles = Role.query.all()
    return {"data": db_roles}


@admin_bp.get("/permission/list")
@admin_bp.output(PermissionSchema(many=True))
def permissions():
    permissions = Permission.query.filter_by(parent_id=None).all()
    return {"code": 0, "data": permissions}


@admin_bp.get("/role/<int:id>/permission")
def role_permission(id):
    permissions = Role.query.get(id).permissions
    data = [p.permission_id for p in permissions]
    return {"data": data, "code": 0}


@admin_bp.post("/role/<int:id>/permission")
@admin_bp.input(SetPermissionIn)
def set_role_permission(id, data):
    role = Role.query.get(id)
    r_p = []
    for p_id in data["permissions"]:
        p = Permission.query.filter_by(permission_id=p_id).first()
        r_p.append(p)
    role.permissions = r_p
    db.session.commit()
    return {"code": 0}
