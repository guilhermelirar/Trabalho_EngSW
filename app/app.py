import os
from pathlib import Path

from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user

from app.models import db
from app.routes.auth_routes import auth_bp
from app.services.AuthService import get_user_by_id

# Pasta onde está este arquivo (raiz do projeto).
# Templates e static são procurados aqui, independente de onde o Flask foi iniciado.
BASE_DIR = Path(__file__).resolve().parent


def create_app():
    """
    Função que cria a instância Flask de acordo com
    a configuração especificada.
    """
    template_dir = BASE_DIR / "templates"
    static_dir = BASE_DIR / "static"

    app = Flask(
        __name__,
        template_folder=str(template_dir),
        static_folder=str(static_dir),
    )
    login_manager = LoginManager()

    # Configuração de banco de dados de desenvolvimento
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Necessária para a sessão do Flask-Login e para as mensagens flash.
    # Em produção, defina a variável de ambiente SECRET_KEY.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-troque-esta-chave')

    # Iniciando extensões
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # type: ignore
    login_manager.login_message = 'Faça login para acessar esta página.'
    login_manager.login_message_category = 'erro'

    with app.app_context():
        db.create_all()

    # Registrando as rotas
    app.register_blueprint(auth_bp)

    @login_manager.user_loader
    def login_user_loader(user_id):
        return get_user_by_id(user_id)

    # Rota raiz: painel se estiver logado, senão login
    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("auth.painel"))
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
