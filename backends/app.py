from apiflask import APIFlask

from config import DevConfig
from admin_bp import admin_bp
from ext import db

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
    return {
        'code': error.status_code,
        'error': error.message,
        'detail': error.detail
    }, 200, error.headers


@app.get("/")
def say_hello():
    return {"message": "Hello!"}
