# tests/test_auth_service.py
"""
Testes unitários para as funções do serviço de autenticação
"""

from flask import Flask
import pytest
from app.services.AuthService import *
from app.services.exceptions import UserCreationException

VALID_EMAIL = "alice@sub.domain.com"
VALID_PWORD = "password123"

def test_register_user_success(app: Flask):
    # (US-002 Success) Criação de usuário com email e senha válidos
    with app.app_context():
        user = register_user(name="alice", 
                             email=VALID_EMAIL, 
                             plain_password=VALID_PWORD)
        assert user.id is not None
        assert user.email == VALID_EMAIL
        assert user.password_hash != VALID_PWORD # senha é criptografada

def test_register_duplicate_email_raises_exception(app: Flask):
    # (US-002 Fail) Email já existente gera erro de criação de usuário
    with app.app_context():
        register_user(name="alice", 
                      email=VALID_EMAIL, 
                      plain_password=VALID_PWORD)
        with pytest.raises(UserCreationException) as exc_info:
            register_user(name="bob", email=VALID_EMAIL, 
                          plain_password=VALID_PWORD)

        assert "E-mail já cadastrado" in exc_info.value.message
        
def test_register_user_invalid_email(app: Flask):
    with app.app_context(), pytest.raises(UserCreationException, 
                                          match="E-mail em formato inválido"):
        register_user(name="alice", 
                      email="invalid email", 
                      plain_password=VALID_PWORD)

        

