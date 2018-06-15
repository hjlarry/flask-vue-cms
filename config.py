SENTRY_URL = 'https://016ce4d019544bfc96e58a925e65c915:150f2c0e5567487298f633ae419bd290@sentry.io/1188584'

GITHUB_OAUTH_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_URL = 'https://api.github.com/user?'
GITHUB_CLIENTID = '9f24e95ba9507c804669'
GITHUB_CLIENTSECRET = '6b09f3cb99b0e8d4df8793450cd2cfc32e587896'

ALLOW_CORS = True


class Config:
    DEBUG = False

    SITE_URL = 'http://localhost:8100/'
    STATIC_FOLDER = 'static'
    STATIC_URL = SITE_URL + STATIC_FOLDER + '/'
    UPLOAD_FOLDER = STATIC_FOLDER + '/upload/'

    SWAGGER = {
        'uiversion': 3
    }

    REDIS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 0
    EXPIRE_TIME = 36000
    FREEZER_IGNORE_MIMETYPE_WARNINGS = True


class DevelopConfig(Config):
    ENV = 'dev'
    DEBUG = True
    SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/internation_card'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    DATABASE_QUERY_TIMEOUT = 0.5


class TestConfig(Config):
    DEBUG = False
    SECRET_KEY = 'thisistest'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    DATABASE_QUERY_TIMEOUT = 0.5


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x81'
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:1234flask@127.0.0.1:3306/internation_freecard'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
