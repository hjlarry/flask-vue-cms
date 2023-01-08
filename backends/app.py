from apiflask import APIFlask
from flask import current_app

from utils import generate_token, auth_cache
from schemas import LoginSchema
from config import DevConfig
from admin_bp import admin_bp
from ext import db
from models import User

from init_data import init_data


def create_app():
    app = APIFlask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        init_data(db)

    app.register_blueprint(blueprint=admin_bp)

    return app


app = create_app()


@app.error_processor
def my_error_processor(error):
    return (
        {"code": error.status_code, "error": error.message, "detail": error.detail},
        200,
        error.headers,
    )


@app.get("/")
def say_hello():
    return {"message": "Hello!"}


@app.post("/admin/login")
@app.input(LoginSchema)
def login(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.verify_password(data["password"]):
        token = generate_token(user.id).decode()
        res = {"data": {"token": token}, "code": 0}
        auth_cache.setex(user.id, current_app.config["EXPIRE_TIME"], token)
        return res
    return {"error": "用户名或密码错误", "code": 1234}
