from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()
swagger = Swagger(template_file='swagger.yml')
