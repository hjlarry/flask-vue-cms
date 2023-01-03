from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf


from config import DevConfig
from models import User, Role
from ext import db

app = APIFlask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

    user1 = User(username='John',password=123, name='John Doe')
    user2 = User(username='admin',password=123, name='Admin Doe')
    role = Role(name='超级管理员', can_edit=False)
    user1.roles.append(role)
    user2.roles.append(role)
    db.session.add_all([user1, user2, role])

    db.session.commit()

@app.get('/')
def say_hello():
    return {'message': 'Hello!'}