# tests/conftest.py
import pytest
from app.app import create_app # importar factory do app
from app.app import db
from app.models.User import User
from app.services.AuthService import register_user

@pytest.fixture
def app():
    _app = create_app()

    # aplicando configurações de teste
    _app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "dev_test_secret_key"
    })

    with _app.app_context():
        db.create_all()
        yield _app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def authenticated_client(client, app):
    with app.app_context():
        # criando usuário no banco de dados
        user = register_user("user", "user@email.com", "password123")
        user_id = str(user.id)

    # injetar flask-login na sessão
    with client.session_transaction() as sess:
        sess['_user_id'] = user_id

    return client
