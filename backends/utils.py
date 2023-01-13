import shelve
import time

from flask import current_app
from apiflask.exceptions import abort
from authlib.jose import jwt

from models import User


class CacheDict:
    def __init__(self, db="cache.db"):
        self.db = db

    def get(self, key, default=None):
        key = str(key)
        with shelve.open(self.db) as db:
            if not key in db:
                return default
            elif db[key].get("expires", 0) < time.time():
                return default
            return db[key]["value"]

    def set(self, key, value):
        key = str(key)
        with shelve.open(self.db) as db:
            db[key] = {"value": value}

    def expire(self, key, expire):
        key = str(key)
        with shelve.open(self.db, writeback=True) as db:
            db[key]["expires"] = time.time() + expire

    def delete(self, key):
        key = str(key)
        with shelve.open(self.db) as db:
            del db[key]

    def setex(self, key, time, value):
        self.set(key, value)
        self.expire(key, time)


auth_cache = CacheDict()


def generate_token(user_id):
    header = {
        "alg": "HS256",
    }
    payload = {"user_id": user_id}
    key = current_app.config["SECRET_KEY"]
    return jwt.encode(header, payload, key)


def verify_token(token):
    key = current_app.config["SECRET_KEY"]
    try:
        data = jwt.decode(token, key)
    except:
        return False
    if "user_id" in data and auth_cache.get(data["user_id"]):
        auth_cache.expire(data["user_id"], current_app.config["EXPIRE_TIME"])
        current_user = User.query.get(data["user_id"])
        return current_user
    return False


permission_cache = CacheDict("permission.db")
from functools import wraps


class PermissionControl:
    def __init__(self, auth):
        self.auth = auth

    def get_permissions(self):
        permissions = permission_cache.get(self.auth.current_user.id)
        if permissions:
            return permissions
        menus = set()
        points = set()
        for role in self.auth.current_user.roles:
            menus.update(
                set(p.permission_mark for p in role.permissions if not p.parent_id)
            )
            points.update(
                set(p.permission_mark for p in role.permissions if p.parent_id)
            )
        permissions = {"menus": menus, "points": points, "all": menus.union(points)}
        permission_cache.set(self.auth.current_user.id, permissions)
        return permissions

    def can(self, permission):
        def wrapper(fn):
            @wraps(fn)
            def decorated_view(*args, **kwargs):
                if permission not in self.get_permissions().get("all"):
                    abort(401)
                return fn(*args, **kwargs)

            return decorated_view

        return wrapper
