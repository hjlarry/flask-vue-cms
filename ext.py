from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

# see http://127.0.0.1:8100/apidocs/ to api doc
swagger = Swagger(template_file='swagger.yml')
