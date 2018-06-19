import redis
from flask_sqlalchemy import SQLAlchemy
from flask_frozen import Freezer
from flask_migrate import Migrate
from flasgger import Swagger
from raven.contrib.flask import Sentry

from flask_server.config import SENTRY_URL, Config
from flask_server.utils import CacheDict

db = SQLAlchemy()
migrate = Migrate(db=db)
freezer = Freezer(with_no_argument_rules=False, log_url_for=False)
swagger = Swagger(template_file='swagger.yml')
sentry = Sentry(dsn=SENTRY_URL)
if Config.REDIS:
    cache = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
else:
    cache = CacheDict()
