from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import redis
from config import Config

db = SQLAlchemy()

# see http://127.0.0.1:8100/apidocs/ to api doc
swagger = Swagger(template_file='swagger.yml')
cache = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
