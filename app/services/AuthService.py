# app/services/AuthService.py
# Criação e login de contas
from pydoc import plain

from services.ServiceErrors import UserCreationException
from models.User import User
from models import db
import re
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

def validate_email(email: str) -> None:
    """
    Valida se email tem menos de 100 caracteres e segue formato padrão usuario@email
    """
    EMAIL_MAX_LEN = 100
    EMAIL_REGEX = r'/^[\w-\.]+@([\w-]+\.)+[\w-]{2,}$/'
    if not len(email) < EMAIL_MAX_LEN or not re.match(EMAIL_REGEX, email):
        raise UserCreationException("Email em formato inválido")

def register_user(name: str | None, email: str | None, plain_password: str | None) -> None:
    """
    Valida dados do usuário passados como argumento e tenta criar um
    objeto de User e salvá-lo no banco de dados. Em caso de erro irá
    levantar uma UserCreationException. Em caso de sucesso retorna None
    """
    if not email or not name or not plain_password:
        raise UserCreationException(message="Dados ausentes")

    validate_email(email)

    if (len(name) > 100):
        raise UserCreationException(message="Nome muito longo (+100 caracteres)")

    if (len(plain_password) < 8):
        raise UserCreationException(message="Senha com menos de 8 caracteres")

    password_hash = generate_password_hash(plain_password)

    new_user = User()
    new_user.name = name
    new_user.email = email
    new_user.password_hash = password_hash

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise UserCreationException("Email já em uso")
