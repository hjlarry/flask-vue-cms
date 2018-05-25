from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import redis
from raven.contrib.flask import Sentry

from config import Config
from utils import CacheDict

db = SQLAlchemy()
if Config.REDIS:
    cache = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
else:
    cache = CacheDict()
# see http://your host/apidocs/ to api doc
swagger = Swagger(template_file='swagger.yml')
sentry = Sentry(dsn=Config.SENTRY_URL)
