from flask_server.ext import db

from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

Column = db.Column
relationship = db.relationship


class BaseModel(db.Model):
    __abstract__ = True

    id = Column('id', db.Integer, primary_key=True)
    _created_at = Column('created_at', db.DateTime, default=datetime.now)
    _updated_at = Column('updated_at', db.DateTime, default=datetime.now, onupdate=datetime.now)
    default_json_fields = []

    @hybrid_property
    def updated_at(self):
        return self._updated_at.strftime('%Y-%m-%d %H:%M:%S') if self._updated_at else None

    @hybrid_property
    def created_at(self):
        return self._created_at.strftime('%Y-%m-%d %H:%M:%S')

    def to_json(self, child_num=None, fields=None):
        """
        将模型中的json_fields字段转化为JSON显示，判断如果是一对多关系显示子模型中的json_fields
        :param child_num: int
        :param json_fields: list
        :return: dict
        """
        res = {}
        json_fields = self.default_json_fields if not fields else fields
        for k in json_fields:
            if k in self.__mapper__.relationships.keys():
                res[k] = []
                for c in getattr(self, k)[:child_num]:
                    res[k].append(c.to_json())
            else:
                res[k] = getattr(self, k)
        return res

    @classmethod
    def get(cls, num=None, child_num=None):
        """
        :param num: int or str('all')
        :param child_num: int
        :return: array
        """
        items = cls.get_item(num)
        return [item.to_json(child_num) for item in items]

    @classmethod
    def get_item(cls, num=None):
        """
        执行模型查询，有排序字段时加入排序字段进行查询
        :param num: int or str('all'), if None means 1
        :return: list
        """
        if hasattr(cls, 'order'):
            order = 'order'
        else:
            order = 'updated_at'

        if num is 'all':
            items = cls.query.order_by(order).all()
            return items
        elif num is None:
            num = 1
        items = cls.query.order_by(order)[:num]
        return items

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update an exist record and save it """
        for attr, value in kwargs.items():
            try:  # 部分属性无法setattr，例如hybird
                setattr(self, attr, value)
            except:
                pass
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record to database."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Article(BaseModel):
    __tablename__ = 'articles'
    title = Column('title', db.String(40))
    content = Column('content', db.Text)
    thumb_pic = Column('thumb_pic', db.String(100))
    order = Column('order', db.Integer)
    module_id = Column('module_id', db.Integer, db.ForeignKey('modules.id'))

    default_json_fields = ['title', 'order', 'id', 'thumb_pic', 'summary', 'updated_at', 'module_name', 'module_id']

    @hybrid_property
    def summary(self):
        return self.content[:100]

    @hybrid_property
    def module_name(self):
        return str(self.module) if self.module else ''


class Module(BaseModel):
    __tablename__ = 'modules'
    order = Column('order', db.Integer)
    title = Column('title', db.String(40))
    template_id = Column('template_id', db.String(40))
    child = relationship('Article', backref='module', lazy='dynamic')
    default_json_fields = ['order', 'template_id', 'id', 'child', 'title']

    def __repr__(self):
        return self.title


class Admin(BaseModel):
    __tablename__ = 'admin_users'
    username = Column('username', db.String(40))
    _password = Column('password', db.String(100))
    name = Column('name', db.String(40))
    avatar = Column('avatar', db.String(100))
    operations = relationship('OperationLog', backref='admin', lazy='dynamic')
    default_json_fields = ['id', 'username', 'name', 'avatar', 'updated_at']

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)

    def verify_password(self, password):
        try:
            result = check_password_hash(self.password, password)
        except:
            return False
        return result

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def __repr__(self):
        return self.name


class OperationLog(BaseModel):
    __tablename__ = 'admin_operation_log'
    user_id = Column('user_id', db.Integer, db.ForeignKey('admin_users.id'))
    path = Column('path', db.String(40))
    method = Column('method', db.String(15))
    ip = Column('ip', db.String(15))
    input = Column('input', db.JSON)
    default_json_fields = ['id', 'user', 'path', 'method', 'ip', 'input_summary', 'created_at']

    @hybrid_property
    def user(self):
        return str(self.admin) if self.admin else ''

    @hybrid_property
    def input_summary(self):
        return str(self.input)[:300] if self.input else ''


class ExpressionOffical(BaseModel):
    __tablename__ = 'expression_offical'
    name = Column('name', db.String(40))
    tel = Column('tel', db.String(40))
    phone_model = Column('phone_model', db.String(40))
    destination = Column('destination', db.String(40))
    departure_time = Column('departure_time', db.String(40))
    return_time = Column('return_time', db.String(40))
    airport = Column('airport', db.String(40))
    terminal = Column('terminal', db.String(40))
