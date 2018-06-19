import multiprocessing
from fabric import Connection
from invoke import task

from flask_server.app import create_app
from flask_server.config import ProdConfig
from flask_server.ext import freezer

try:
    from fabfile import HOST, PORT, USERNAME, PASSWORD
except ModuleNotFoundError:
    HOST, PORT, USERNAME, PASSWORD = '', '', '', ''
connect = Connection(HOST, user=USERNAME, port=PORT, connect_kwargs={'password': PASSWORD})
DEPLOY_DIR = '/home/www/flask-vue-cms'
prod_app = create_app(ProdConfig)


@task
def deploy(c):
    pull_res = connect.run('cd ' + DEPLOY_DIR + ' && git pull')
    print(pull_res)
    stop_service = connect.sudo('supervisorctl -c /etc/supervisord.conf stop cms')
    print(stop_service)
    start_service = connect.sudo('supervisorctl -c /etc/supervisord.conf start cms')
    print(start_service)


@task
def db_init(c):
    c.run('cd flask_server && flask db init')


@task
def db_migrate(c):
    c.run('cd flask_server && flask db migrate')


@task
def db_upgrade(c):
    c.run('cd flask_server && flask db upgrade')


@task
def create_admin(c, username='admin', password='admin'):
    c.run('cd flask_server && flask create_admin --username ' + username + ' --password ' + password)


@task
def rundev(c):
    def run_flask():
        c.run('cd flask_server && flask run -h 0.0.0.0 -p 8100')

    def run_vue():
        c.run('cd admin_with_vue && npm run dev', echo=True)

    t1 = multiprocessing.Process(target=run_flask)
    t2 = multiprocessing.Process(target=run_vue)
    t1.start()
    t2.start()


@task
def test(c):
    c.run('cd flask_server && pytest tests')


@task
def freeze(c):
    """
    会触发一个MissingURLGeneratorWarning的警告，因为只让部分路由生成静态页面了，忽略警告即可。
    """
    freezer.freeze()
