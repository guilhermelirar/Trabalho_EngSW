# tests/test_auth_service.py
"""
Testes unitários para as funções do serviço de autenticação
"""

from flask import Flask
import pytest
from app.services.AuthService import *
from app.services.exceptions import UserCreationException

def test_register_user_success(app: Flask):
    """
    Criação de usuário com email e senha válidos (US-002)
    """
    with app.app_context():
        email = "alice@sub.domain.com"
        password = "password123"
        user = register_user(name="alice", 
                             email=email, 
                             plain_password=password)
        assert user.id is not None
        assert user.email == email
        assert user.password_hash != password # senha é criptografada

        


