# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from flask_server.ext import db
from flask_server.models import Admin, Article, Module


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: 'user{0}'.format(n))
    name = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = Sequence(lambda n: 'hehe{0}'.format(n))
    avatar = Sequence(lambda n: 'http://www.google.com/{0}'.format(n))

    class Meta:
        """Factory configuration."""
        model = Admin


class ArticleFactory(BaseFactory):
    """Article factory."""

    title = Sequence(lambda n: 'article{0}'.format(n))
    content = Sequence(lambda n: 'something{0}'.format(n))
    order = Sequence(lambda n: n)
    thumb_pic = Sequence(lambda n: 'http://www.google.com/{0}'.format(n))

    class Meta:
        """Factory configuration."""
        model = Article


class ModuleFactory(BaseFactory):
    """Module factory."""

    title = Sequence(lambda n: 'Module{0}'.format(n))
    order = Sequence(lambda n: n)

    class Meta:
        """Factory configuration."""
        model = Module
