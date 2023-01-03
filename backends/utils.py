import shelve
import time

from flask import current_app
from authlib.jose import jwt

from models import User

class CacheDict():
    def __init__(self, db='cache.db'):
        self.db = db

    def get(self, key, default=None):
        key = str(key)
        with shelve.open(self.db) as db:
            if not key in db:
                return default
            elif db[key].get('expires', 0) < time.time():
                return default
            return db[key]['value']

    def set(self, key, value):
        key = str(key)
        with shelve.open(self.db) as db:
            db[key] = {
                'value': value
            }

    def expire(self, key, expire):
        key = str(key)
        with shelve.open(self.db, writeback=True) as db:
            db[key]['expires'] = time.time() + expire

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
