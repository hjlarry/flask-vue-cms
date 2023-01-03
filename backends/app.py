from apiflask import APIFlask, Schema, abort, HTTPTokenAuth
from apiflask.fields import Integer, String, List, Nested
from apiflask.validators import Length, OneOf
from flask import current_app

from config import DevConfig
from models import User, Role
from ext import db
from utils import generate_token, auth_cache, verify_token

app = APIFlask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')
auth.verify_token(verify_token)
app.config.from_object(DevConfig)
db.init_app(app)

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

@app.post('/login')
@app.input(LoginScheme)
def login(data):
    user = User.query.filter_by(username=data['username']).first()
    if user and user.verify_password(data["password"]):
        token = generate_token(user.id).decode()
        res = {"data": {"token": token}}
        auth_cache.setex(user.id, current_app.config["EXPIRE_TIME"], token)
        return res
    return {'error': '用户名或密码错误'}

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

@app.get('/info')
@app.output(schema=UserInfoScheme)
@app.auth_required(auth)
def get_info():
    return auth.current_user