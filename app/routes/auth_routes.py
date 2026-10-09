# auth_routes.py
# Rotas para interação com serviços de autenticação
# Criar usuário e login

from flask import Blueprint, Request, Response, render_template, request, flash, redirect, url_for
from app.services.ServiceErrors import ServiceException, UserCreationException
from services import AuthService as auth_srv
auth_bp = Blueprint('auth', __name__)

# LOGIN

@auth_bp.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

# CRIAR USUÁRIO

@auth_bp.route('/login', methods=['GET', 'POST'])
def post_register():
    """
    Rota para criar usuário.
    Obtem name, email, password por meio de request.form e chama o serviço de
    criação de usuário.
    """
    if request.method == 'GET':
        return render_template('register.html')

    # tenta criar usuário
    auth_srv.register_user(
      name = request.form.get('name'),
      email = request.form.get('email'),
      plain_password = request.form.get('plain_password')
    )

    # se não levantar exceção
    flash(f"Conta criada com sucesso! Faça login para continuar", "success")

    return redirect(url_for('register.html'))

@auth_bp.errorhandler(UserCreationException)
def register_fail(error):
    """
    Criação de usuário resultou em erro (usuário já existe, ou erro de formato)
    """
    form_data = request.form.to_dict()
    form_data.pop('password', None)

    flash(error.message, "danger")

    return render_template('register', **form_data), 400
