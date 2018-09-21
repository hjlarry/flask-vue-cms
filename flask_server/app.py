from flask import Flask, render_template, Response, current_app
from flask_sqlalchemy import get_debug_queries
from flask.cli import with_appcontext
import click
import logging
from logging.handlers import RotatingFileHandler

from flask_server.ext import db, swagger, sentry, freezer, migrate
from flask_server.utils import ApiResult, ApiException
from flask_server.api import api_bp
from flask_server.admin import admin_bp
from flask_server.config import DevelopConfig
from flask_server.models import Admin


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


@click.command()
@click.option('--username', default='admin')
@click.option('--password', default='admin')
@with_appcontext
def create_admin(username, password):
    try:
        Admin.create(username=username, password=password)
        print('success')
    except Exception as e:
        print(e)


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


def register_logger(app):
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(process)d %(thread)d '
        '%(pathname)s %(lineno)s %(message)s')

    class InfoFilter(logging.Filter):
        def filter(self, record):
            if logging.INFO <= record.levelno < logging.ERROR:
                return super().filter(record)
            else:
                return 0

    # FileHandler Info
    file_handler_info = RotatingFileHandler(filename='info.log')
    file_handler_info.setFormatter(formatter)
    file_handler_info.setLevel(logging.INFO)
    info_filter = InfoFilter()
    file_handler_info.addFilter(info_filter)

    # FileHandler Error
    file_handler_error = RotatingFileHandler(filename='error.log')
    file_handler_error.setFormatter(formatter)
    file_handler_error.setLevel(logging.ERROR)

    app.logger.addHandler(file_handler_error)
    app.logger.addHandler(file_handler_info)


def create_app(config=DevelopConfig):
    app = ApiFlask(__name__, static_folder='static')
    app.config.from_object(config)

    register_ext(app)
    register_blueprint(app)
    register_errorhandler(app)
    app.cli.add_command(create_admin)
    register_logger(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        for query in get_debug_queries():
            if query.duration > current_app.config['DATABASE_QUERY_TIMEOUT']:
                app.logger.warning('SLOW QUERY: {}\nParameters: {}\nDuration: {}\nContext: {}\n'
                                   .format(query.statement, query.parameters, query.duration, query.context))
        return response

    app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.ico'))

    return app


app = create_app()
