from itsdangerous import JSONWebSignatureSerializer as Serializer
from flask import current_app, json, request
import time
import os

from .bp import admin_bp, allowed_file, secure_filename, CH_REGEX
from models import Admin
from utils import success, fail
from redis_db import cache
from config import EXPIRE_TIME, UPLOAD_FOLDER
from ext import db


def generate_token(user_id):
    serializer = Serializer(current_app.config['SECRET_KEY'])
    return serializer.dumps({'user_id': user_id})


def verify_token(token):
    serializer = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = serializer.loads(token)
    except:
        return False
    if 'user_id' in data and cache.get(data['user_id']):
        cache.expire(data['user_id'], EXPIRE_TIME)
        return data
    return False


@admin_bp.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)
    except:
        return fail(401)
    user = Admin.query.filter_by(username=data['username']).first()
    if user and user.verify_password(data['password']):
        token = generate_token(user.id).decode()
        res = {'data':
                   {'token': token}}
        cache.set(user.id, token)
        cache.expire(user.id, EXPIRE_TIME)
        return success(res)
    return fail(401)


@admin_bp.route('/logout', methods=['POST'])
def logout():
    data = verify_token(request.headers['Authorization'])
    cache.delete(data['user_id'])
    return success()


@admin_bp.route('/info')
def info():
    token = request.args.get('token')
    data = verify_token(token)
    user = Admin.query.get_or_404(data['user_id'])
    if not user:
        return fail(401)
    res = {
        'data':{
            'name': user.name,
            'avatar': user.avatar
        }
    }
    return success(res)


@admin_bp.route('/user')
def users():
    current_page = request.args.get('page') or 1
    per_page = request.args.get('limit') or 10
    pagination = Admin.query.paginate(int(current_page), per_page=int(per_page))
    users = pagination.items
    total = pagination.total
    result = []
    for item in users:
        item = item.to_json()
        result.append(item)

    res = {
        'data': {
            'items': result,
            'total': total
        }
    }
    return success(res)


@admin_bp.route('/user/<int:id>')
def get_user(id):
    user = Admin.query.get_or_404(id)
    res = {
        'data': user.to_json()
    }
    return success(res)


@admin_bp.route('/user/create', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = Admin(username=data['username'], name=data['name'], avatar=data['avatar'])
    user.generate_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return success()


@admin_bp.route('/user/edit', methods=['POST'])
def edit_user():
    data = json.loads(request.data)
    user = Admin.query.get_or_404(data['id'])
    user.name=data['name']
    user.avatar=data['avatar']
    if data['password']:
        user.generate_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return success()


@admin_bp.route('/user/delete', methods=['POST'])
def delete_user():
    data = json.loads(request.data)
    user = Admin.query.get_or_404(data['id'])
    if user:
        db.session.delete(user)
        db.session.commit()
        return success()
    return fail(400)


@admin_bp.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    file = request.files['avatar']
    if file:
        now = time.time()
        filename = str(int(now)) + file.filename
        if not allowed_file(filename):
            return fail(415)
        if not CH_REGEX.search(filename):
            filename = secure_filename(filename)
        UPLOAD_PATH = os.path.join(UPLOAD_FOLDER, 'avatar')
        filepath = os.path.join(UPLOAD_PATH, filename)
        file.save(filepath)

        res = {'data':
                   {
                       'filename': filename,
                        'fileurl': filepath
                    }
               }
        return success(res)
    return fail(400)