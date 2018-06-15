import multiprocessing
from fabric import Connection
from invoke import task
from flask_sqlalchemy import get_debug_queries
from flask import current_app

from flask_server.app import create_app
from flask_server.config import DevelopConfig

try:
    from fabfile import HOST, PORT, USERNAME, PASSWORD
except ModuleNotFoundError:
    HOST, PORT, USERNAME, PASSWORD = '', '', '', ''
connect = Connection(HOST, user=USERNAME, port=PORT, connect_kwargs={'password': PASSWORD})
DEPLOY_DIR = '/home/www/flask-vue-cms'


@task
def deploy(c):
    pull_res = connect.run('cd ' + DEPLOY_DIR + ' && git pull')
    print(pull_res)
    stop_service = connect.sudo('supervisorctl -c /etc/supervisord.conf stop cms')
    print(stop_service)
    start_service = connect.sudo('supervisorctl -c /etc/supervisord.conf start cms')
    print(start_service)


def develop_app():
    app = create_app(DevelopConfig)

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

    return app


@task
def rundev(c):
    def run_flask():
        app = develop_app()
        app.run(host='0.0.0.0', port=8100)

    def run_vue():
        c.run('cd admin_with_vue && npm run dev', echo=True)

    t1 = multiprocessing.Process(target=run_flask)
    t2 = multiprocessing.Process(target=run_vue)
    t1.start()
    t2.start()
