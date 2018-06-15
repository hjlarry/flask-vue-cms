# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from flask_server.models import Admin, Article, Module

from .factories import UserFactory, ArticleFactory


@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_get_by_id(self):
        """Get user by ID."""
        user = Admin(username='foo', password='foo@bar.com')
        user.save()

        retrieved = Admin.query.get_or_404(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        user = Admin(username='foo', password='foo@bar.com')
        user.save()
        assert bool(user._created_at)
        assert isinstance(user._created_at, dt.datetime)

    def test_password_is_nullable(self):
        """Test null password."""
        user = Admin(username='foo')
        user.save()
        assert user.password is None

    def test_factory(self, db):
        """Test user factory."""
        user1 = UserFactory(password='myprecious')
        user2 = UserFactory()
        db.session.commit()
        assert bool(user1.username)
        assert bool(user1.name)
        assert bool(user1.created_at)
        assert bool(user2.password)
        assert user1.verify_password('myprecious')

    def test_check_password(self):
        """Check password."""
        user = Admin.create(username='foo', name='foo@bar.com', password='foobarbaz123')
        assert user.verify_password('foobarbaz123') is True
        assert user.verify_password('barfoobaz') is False


@pytest.mark.usefixtures('db')
class TestArticle:
    """Article tests."""

    def test_get_by_id(self):
        """Get Article by ID."""
        article = Article(title='foo', content='somethingstrange')
        article.save()

        retrieved = Article.query.get_or_404(article.id)
        assert retrieved == article

    def test_factory(self, db):
        """Test Article factory."""
        article = ArticleFactory()
        db.session.commit()
        assert bool(article.title)
        assert bool(article.content)
        assert isinstance(article.order, int)
        assert bool(article.thumb_pic)


@pytest.mark.usefixtures('db')
class TestModule:
    """Module tests."""

    def test_get_by_id(self):
        """Get Module by ID."""
        module = Module(title='foo', order=5, template_id='i_1')
        module.save()

        retrieved = Module.query.get_or_404(module.id)
        assert retrieved == module

    def test_add_article_with_module(self):
        """Add a module to an article."""
        module = Module(title='module_article')
        module.save()
        article = ArticleFactory()
        article.module = module
        article.save()
        assert isinstance(article.module_id, int)

