import pytest

from app.app import create_app, db
from app.models import Project, ProjectBacklog, User
from app.models.acceptance_criteria import AcceptanceCriteria
from app.models.user_story import UserStory
from app.services.auth_service import register_user


@pytest.fixture
def app():
    _app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "WTF_CSRF_ENABLED": False,
            "SECRET_KEY": "dev_test_secret_key",
        }
    )

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
        sess["_user_id"] = user_id

    return client


@pytest.fixture
def test_user(app):
    """Cria um usuário padrão para os testes dentro do app_context."""
    user = User()
    user.name = "Test"
    user.email = "test@example.com"
    user.password_hash = "hashedpw"
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def project_with_backlog(app, test_user):
    """Cria um projeto vinculado ao usuário e com um ProductBacklog ativo."""
    project = Project()
    project.name = "Sistema de Gestão"
    project.description = "Projeto de teste para EngSW"
    project.user_id = test_user.id

    db.session.add(project)
    db.session.commit()

    backlog = ProjectBacklog()
    backlog.project_id = project.id

    db.session.add(backlog)
    db.session.commit()

    return project


@pytest.fixture
def existing_user_story(app, project_with_backlog):
    """Cria história de usuário dentro de um projeto existente"""
    us = UserStory()
    us.project_backlog_id = project_with_backlog.backlog.id
    us.title = "História de usuário"
    us.role = "[Papel]"
    us.action = "[Ação]"
    us.benefit = "[Benefit]"

    db.session.add(us)
    db.session.commit()

    return us
