from flask import Flask, render_template, Response

from flask_server.ext import db, swagger, sentry, freezer, migrate
from flask_server.utils import ApiResult, ApiException
from flask_server.api import api_bp
from flask_server.admin import admin_bp
from flask_server.config import DevelopConfig


class ApiFlask(Flask):
    def make_response(self, rv: dict or ApiResult) -> Response:
        if isinstance(rv, dict):
            if 'code' not in rv:
                rv['code'] = 0
                rv['msg'] = 'success'
            rv = ApiResult(rv)
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


def register_ext(app):
    db.init_app(app)
    swagger.init_app(app)
    sentry.init_app(app)
    freezer.init_app(app)
    migrate.init_app(app)


def register_blueprint(app):
    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)


def register_errorhandler(app):
    @app.errorhandler(ApiException)
    def api_error_handler(error):
        return error.to_result()

    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_handler(error):
        if hasattr(error, 'name'):
            msg = error.name
            status = error.code
        else:
            msg = 'error'
            status = 500
        value = {'message': msg, 'code': 1}
        return ApiResult(value, status)


def create_app(config):
    app = ApiFlask(__name__, static_folder='static')
    app.config.from_object(config)

    register_ext(app)
    register_blueprint(app)
    register_errorhandler(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.ico'))

    return app

# only for flask migrate commands run
app = create_app(DevelopConfig)
