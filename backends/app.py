from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf


from config import DevConfig
from models import Address, User
from ext import db

app = APIFlask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

    user = User(name='John', fullname='John Doe')
    db.session.add(user)
    db.session.commit()

@app.get('/')
def say_hello():
    return {'message': 'Hello!'}