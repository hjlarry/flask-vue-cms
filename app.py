from flask import Flask, render_template, Response, current_app
from flask_sqlalchemy import get_debug_queries

from ext import db, swagger, sentry
from utils import ApiResult, ApiException
from api import api_bp
from admin import admin_bp

import config


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


def create_app(config):
    app = ApiFlask(__name__, static_folder=config.STATIC_FOLDER)
    app.config.from_object(config)

    db.init_app(app)
    swagger.init_app(app)
    sentry.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)

    return app


app = create_app(config.DevelopConfig)


# For local test env
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


@app.route('/')
def index():
    return render_template('index.html')


app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.ico'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=app.debug)
