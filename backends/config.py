from schemas import BaseResponse


class DevConfig:
    SECRET_KEY = "\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/flask"
    EXPIRE_TIME = 36000
    BASE_RESPONSE_SCHEMA = BaseResponse
    BASE_RESPONSE_DATA_KEY = "data"