from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import redis
from raven.contrib.flask import Sentry

from config import Config

db = SQLAlchemy()
cache = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
# see http://your host/apidocs/ to api doc
swagger = Swagger(template_file='swagger.yml')
sentry = Sentry(dsn='https://016ce4d019544bfc96e58a925e65c915:150f2c0e5567487298f633ae419bd290@sentry.io/1188584')




