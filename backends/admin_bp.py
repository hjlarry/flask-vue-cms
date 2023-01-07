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
    return {"code": 0}


@admin_bp.post('/user/delete/<int:id>')
def delete_user(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"code": 2000, "error": "some data delete error!"}
    return {"code": 0}


@admin_bp.get('/user/<int:id>')
def get_user(id):
    data = {
        "role": [
            {
                "id": "1",
                "title": "超级管理员"
            }
        ],
        "remark": [
            "超级管理员",
            "BOSS"
        ],
        "experience": [
            {
                "startTime": "2016-05-24",
                "endTime": "2017-05-24",
                "title": "慕课网",
                "desc": "混合开发京东商城"
            },
            {
                "startTime": "2018-06-01",
                "endTime": "2019-08-12",
                "title": "慕课网",
                "desc": "uni-app 开发企业级小程序"
            }
        ],
        "_id": "612710a0ec87aa543c9c341d",
        "id": "0",
        "openTime": "2016-05-24",
        "username": "super-admin",
        "title": "超级管理员",
        "mobile": "188xxxx0001",
        "avatar": "https://m.imooc.com/static/wap/static/common/img/logo-small@2x.png",
        "gender": "男",
        "province": "北京",
        "nationality": "汉",
        "address": "北京市朝阳区xx大道 11xx0 号 3 层",
        "major": "在线职业教育平台",
        "glory": "国内领先的线上 IT 教育品牌"
    }
    return {"code": 0, "data": data}


@admin_bp.get('/role/list')
def roles():
    data = [
        {
            "id": "1",
            "title": "超级管理员",
            "describe": "唯一账号，可以操作系统所有功能"
        },
        {
            "id": "2",
            "title": "管理员",
            "describe": "由超管指定，可以为多个，协助超管管理系统"
        },
        {
            "id": "3",
            "title": "人事经理",
            "describe": "主管人事相关业务"
        },
        {
            "id": "4",
            "title": "销售经理",
            "describe": "主管销售相关业务"
        },
        {
            "id": "5",
            "title": "保安队长",
            "describe": "主管安保相关业务"
        },
        {
            "id": "6",
            "title": "员工",
            "describe": "普通员工"
        }
    ]
    return {"code": 0, "data": data}


@admin_bp.get('/permission/list')
def permissions():
    data = [
        {
            "id":"1",
            "permissionName":"员工管理",
            "permissionMark":"userManage",
            "permissionDesc":"员工管理菜单",
            "children":[
                {
                    "id":"1-1",
                    "permissionName":"分配角色",
                    "permissionMark":"distributeRole",
                    "permissionDesc":"为员工分配角色"
                },
                {
                    "id":"1-2",
                    "permissionName":"导入员工",
                    "permissionMark":"importUser",
                    "permissionDesc":"通过 excel 导入员工"
                },
                {
                    "id":"1-3",
                    "permissionName":"删除员工",
                    "permissionMark":"removeUser",
                    "permissionDesc":"删除员工"
                }
            ]
        },
        {
            "id":"2",
            "permissionName":"角色列表",
            "permissionMark":"roleList",
            "permissionDesc":"角色列表菜单",
            "children":[
                {
                    "id":"2-1",
                    "permissionName":"分配权限",
                    "permissionMark":"distributePermission",
                    "permissionDesc":"为角色分配权限"
                }
            ]
        },
        {
            "id":"3",
            "permissionName":"权限列表",
            "permissionMark":"permissionList",
            "permissionDesc":"权限列表菜单",
            "children":[

            ]
        },
        {
            "id":"4",
            "permissionName":"文章排名",
            "permissionMark":"articleRanking",
            "permissionDesc":"文章排名菜单",
            "children":[

            ]
        },
        {
            "id":"5",
            "permissionName":"创建文章",
            "permissionMark":"articleCreate",
            "permissionDesc":"创建文章页面",
            "children":[

            ]
        }
    ]
    return {"code": 0, "data": data}