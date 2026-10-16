# auth_routes.py
# Rotas para interação com serviços de autenticação
# Criar usuário e login

from flask import Blueprint, render_template,\
        request, flash, redirect, url_for
from flask_login import login_user
from app.services.exceptions import LoginException, UserCreationException
import app.services.auth_service as auth_srv
auth_bp = Blueprint('auth', __name__)

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Serve tela de login de usuário, e lida com a ação de login a partir
    de um formulário com os campos:
    - email: str
    - password: str
    """
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash("Formulário inválido", "danger")
        return render_template('login.html', email=email), 400

    try:
        # caminho de sucesso
        user = auth_srv.authenticate_user(email, password)
        login_user(user)
        return redirect(url_for('projects.projects_list'))

    except LoginException as error:
        # usuário ou senha incorretos
        flash(error.message, "danger")
        return render_template('login.html', email=email), 401

# REGISTER (criar usuário)
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Rota para criar usuário.
    Obtem name, email, password por meio de request.form e chama o serviço de
    criação de usuário. Formulário contém:
    name: str
    email: str
    password: str
    """
    if request.method == 'GET':
        return render_template('register.html')

    name = request.form.get('name')
    email = request.form.get('email')
    plain_password = request.form.get('password')

    # tenta criar usuário
    try:
        auth_srv.register_user(name, email, plain_password)
        flash(f"Conta criada com sucesso! Faça login para continuar", "success")
        return redirect(url_for('auth.login'))

    except UserCreationException as error:
        # dados inválidos
        flash(error.message, "danger")
        return render_template('register.html', name=name, email=email), 400
