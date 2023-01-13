from apiflask import HTTPTokenAuth, APIBlueprint, pagination_builder
from flask import request

from utils import verify_token, PermissionControl
from schemas import (
    UserInfoSchema,
    UserDetailSchema,
    ListQuery,
    UsersOut,
    ImportUser,
    RoleSchema,
    PermissionSchema,
    SetPermissionIn,
    ArticleSchema,
    ArticlesOut,
    ArticleIn,
)
from ext import db
from models import User, Role, Permission, Article

admin_bp = APIBlueprint("admin", __name__, url_prefix="/admin")
auth = HTTPTokenAuth(scheme="Bearer")
auth.verify_token(verify_token)
permission = PermissionControl(auth)


@admin_bp.before_request
@admin_bp.auth_required(auth)
def whole_bp_need_login():
    pass


@admin_bp.get("/info")
@admin_bp.output(schema=UserInfoSchema)
def get_info():
    p = permission.get_permissions()
    data = {"menus": list(p.get("menus")), "points": list(p.get("points"))}
    auth.current_user.__dict__["permissions"] = data
    return {"data": auth.current_user}


@admin_bp.get("/feature")
def get_feature():
    data = [
        {
            "title": "Vue3(V3.2.*)",
            "percentage": 100,
            "content": '项目基于最新的vue3标准进行开发，全面使用最新的的<a target="_blank" href="https://github.com/vuejs/rfcs/blob/master/active-rfcs/0040-script-setup.md">RFC script setup</a>语法标准，为你带来不一样的 vue3 开发体验',
        },
        {
            "title": "Element-Plus(V2.2.*)",
            "percentage": 100,
            "content": '<a target="_blank" href="https://element-plus.org/#/zh-CN">Element Plus</a>，一套为开发者、设计师和产品经理准备的基于 Vue 3.0 的桌面端组件库。是 Element UI 的官方 vue 3 兼容版本',
        },
        {
            "title": "Pinia(V2.0.*)",
            "percentage": 100,
            "content": "vuex的官方替代品",
        },
        {
            "title": "Vite",
            "percentage": 100,
            "content": "webpack的官方替代品",
        },
        {
            "title": "Flask(V2.2.*)",
            "percentage": 100,
            "content": "最新版flask",
        },
        {
            "title": "ApiFlask(V1.2.*)",
            "percentage": 100,
            "content": "最现代的flask生态中的api框架",
        },
        {
            "title": "sqlalchemy(V2.0.*)",
            "percentage": 100,
            "content": "最新版的sqlalchemy",
        },
        {
            "title": "国际化",
            "percentage": 60,
            "content": "大部分的国际化支持",
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
                "content": '<a target="_blank" href="https://element-plus.org/">Element Plus</a>，Other thing',
            },
        ]
    return {"data": data, "code": 0}


@admin_bp.get("/timeline")
def get_timeline():
    data = [
        {"content": "开始开发", "timestamp": "2018.03", "id": 1},
        {"content": "使用flask的0.12版本，以及vue2版本", "timestamp": "2018.09", "id": 2},
        {
            "content": "使用flaskV2.2,sqlalchemyV2.0,vue3,vite,pinia等新技术重新开发",
            "timestamp": "2022.12",
            "id": 3,
        },
    ]
    return {"data": data, "code": 0}


@admin_bp.get("/user/list")
@admin_bp.input(ListQuery, location="query")
@admin_bp.output(schema=UsersOut)
@permission.can("userManage")
def get_userlist(params):
    paganition = User.query.paginate(page=params["page"], per_page=params["per_page"])
    return_data = {
        "users": paganition.items,
        "pagination": pagination_builder(paganition),
    }
    return {"data": return_data}


@admin_bp.post("/user/batchImport")
@admin_bp.input(ImportUser)
@permission.can("importUser")
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
@permission.can("removeUser")
def delete_user(id):
    if id == 1:
        return {"code": 4000, "error": "can not delete admin!"}
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
@permission.can("distributeRole")
def update_user_role(id, data):
    if id == 1:
        return {"code": 4000, "error": "can not set admin!"}
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
@permission.can("roleList")
def roles():
    db_roles = Role.query.all()
    return {"data": db_roles}


@admin_bp.get("/permission/list")
@admin_bp.output(PermissionSchema(many=True))
@permission.can("permissionList")
def permissions():
    permissions = Permission.query.filter_by(parent_id=None).all()
    return {"code": 0, "data": permissions}


@admin_bp.get("/role/<int:id>/permission")
@permission.can("permissionList")
def role_permission(id):
    permissions = Role.query.get(id).permissions
    data = [p.permission_id for p in permissions]
    return {"data": data, "code": 0}


@admin_bp.post("/role/<int:id>/permission")
@admin_bp.input(SetPermissionIn)
@permission.can("distributePermission")
def set_role_permission(id, data):
    role = Role.query.get(id)
    if not role.can_edit:
        return {"code": 4000, "error": "can not edit this role!"}
    r_p = []
    for p_id in data["permissions"]:
        p = Permission.query.filter_by(permission_id=p_id).first()
        r_p.append(p)
    role.permissions = r_p
    db.session.commit()
    return {"code": 0}


@admin_bp.get("/article/list")
@admin_bp.input(ListQuery, location="query")
@admin_bp.output(schema=ArticlesOut)
@permission.can("articles")
def get_articles(params):
    paganition = Article.query.paginate(
        page=params["page"], per_page=params["per_page"]
    )
    return_data = {
        "articles": paganition.items,
        "pagination": pagination_builder(paganition),
    }
    return {"data": return_data}


@admin_bp.get("/article/<int:id>")
@admin_bp.output(ArticleSchema)
@permission.can("articles")
def get_article(id):
    article = Article.query.get(id)
    return {"data": article}


@admin_bp.post("/article/delete/<int:id>")
@permission.can("articles")
def delete_article(id):
    try:
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"code": 2000, "error": "some data delete error!"}
    return {"code": 0}


@admin_bp.post("/article")
@admin_bp.input(ArticleIn)
@permission.can("articleCreate")
def create_article(data):
    article = Article(**data)
    article.author = auth.current_user
    db.session.add(article)
    db.session.commit()
    return {"code": 0}


@admin_bp.post("/article/<int:id>")
@admin_bp.input(ArticleIn)
@permission.can("articleCreate")
def edit_article(id, data):
    article = Article.query.get(id)
    article.title = data["title"]
    article.content = data["content"]
    db.session.add(article)
    db.session.commit()
    return {"code": 0}
