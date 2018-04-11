# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from app import create_app
from ext import db as _db
from config import TestConfig

from .factories import UserFactory


@pytest.fixture
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.fixture
def testapp_with_auth(app):
    """A Webtest app with auth in http header."""
    app = TestApp(app)
    user = UserFactory(username='admin123', password='admin123')
    user.save()
    res = app.post_json('/admin/login', {'username': 'admin123', 'password': 'admin123'})
    app.extra_environ.update({'Authorization': res.json['data']['token']})
    return app


@pytest.fixture
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = UserFactory(password='myprecious')
    db.session.commit()
    return user
