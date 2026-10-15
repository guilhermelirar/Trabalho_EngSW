# tests/conftest.py
import pytest
from app.app import create_app # importar factory do app
from app.app import db

@pytest.fixture
def app():
    _app = create_app()

    # aplicando configurações de teste
    _app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False
    })

    with _app.app_context():
        db.create_all()
        yield _app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
