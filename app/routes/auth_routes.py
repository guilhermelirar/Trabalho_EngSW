# auth_routes.py 
# Rotas para interação com serviços de autenticação 
# Criar usuário e login

from flask import Blueprint, Request, Response, render_template, request


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')
