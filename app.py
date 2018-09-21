from flask_server.app import create_app
from flask_server.config import ProdConfig
app = create_app(ProdConfig)