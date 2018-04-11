# -*- coding: utf-8 -*-
"""Test configs."""
from app import create_app
from config import DevelopConfig, ProdConfig


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevelopConfig)
    assert app.config['ENV'] == 'dev'
    assert app.config['DEBUG'] is True
