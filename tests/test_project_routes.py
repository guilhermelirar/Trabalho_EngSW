# tests/test_project_routes.py

from flask.testing import FlaskClient

from app.models import Epic, Project, SprintBacklog, UserStory, db


def test_projects_route_handles_unauthenticated(client: FlaskClient):
    # US-005 Fail: acessar sem sessão ativa redireciona para o login
    response = client.get("/projects")
    assert response.status_code == 302
    assert "/login" in response.location


def test_project_routes_succes(authenticated_client: FlaskClient):
    # US-005 Success: acessar com usuário logado retorna página
    response = authenticated_client.get("/projects")
    assert response.status_code == 200  # OK


def test_route_create_project_success(authenticated_client: FlaskClient):
    # US-005 Success: criar um projeto e ser redirecionado para a tela dele
    response = authenticated_client.post("/projects", data={"name": "Projeto 1"})
    assert response.status_code == 302  # Resource created -> Redirect


def test_project_detail_renders_backlog_and_story_actions(
    authenticated_client: FlaskClient,
):
    """A tela do projeto integra os serviços de backlog e histórias."""
    created = authenticated_client.post("/projects", data={"name": "Projeto 1"})

    detail = authenticated_client.get(created.location)
    assert detail.status_code == 200
    assert b"Criar Product Backlog" in detail.data

    backlog = authenticated_client.post(f"{created.location}/backlog")
    assert backlog.status_code == 302

    story = authenticated_client.post(
        f"{created.location}/stories",
        data={
            "title": "Fazer login",
            "role": "usuario",
            "action": "autenticar",
            "benefit": "acessar o sistema",
        },
    )
    assert story.status_code == 302

    board = authenticated_client.get(created.location)
    assert board.status_code == 200
    assert b"Fazer login" in board.data
    assert b"Product Backlog" in board.data


def test_epic_link_and_sprint_removal_preserve_user_stories(
    authenticated_client: FlaskClient, app
):
    """Aba de épicos vincula HUs e remoção de sprint não apaga requisitos."""
    created = authenticated_client.post("/projects", data={"name": "Projeto 1"})
    project_url = created.location
    authenticated_client.post(f"{project_url}/backlog")
    authenticated_client.post(
        f"{project_url}/stories",
        data={
            "title": "Criar conta",
            "role": "usuario",
            "action": "criar uma conta",
            "benefit": "acessar o sistema",
            "story_points": "3",
            "moscow": "C",
            "rice_reach": "10",
            "rice_impact": "1",
            "rice_confidence": "50",
            "rice_effort": "2",
        },
    )
    authenticated_client.post(f"{project_url}/sprints")

    with app.app_context():
        project = Project.query.one()
        story = UserStory.query.one()
        project_id = project.id
        story_id = story.id
        assert story.story_points == 3
        assert story.moscow == "C"
        assert story.rice_effort == 3
        assert story.rice_score == 1.67

    edited = authenticated_client.post(
        f"/stories/{story_id}",
        data={
            "title": "Criar conta",
            "role": "usuario",
            "action": "criar uma conta",
            "benefit": "acessar o sistema",
            "story_points": "8",
            "moscow": "M",
            "rice_reach": "100",
            "rice_impact": "3",
            "rice_confidence": "80",
            "rice_effort": "5",
        },
    )
    assert edited.status_code == 302

    with app.app_context():
        story = db.session.get(UserStory, story_id)
        sprint = SprintBacklog.query.one()
        assert story is not None
        assert story.story_points == 8
        assert story.moscow == "M"
        assert story.rice_effort == 8
        assert story.rice_score == 30
        story.sprint_backlog_id = sprint.id
        db.session.commit()
        sprint_id = sprint.id

    created_epic = authenticated_client.post(
        f"{project_url}/epics", data={"title": "Acesso e autenticação"}
    )
    assert created_epic.status_code == 302

    with app.app_context():
        epic_id = Epic.query.one().id

    linked = authenticated_client.post(
        f"{project_url}/epics/{epic_id}/stories/link", data={"story_id": story_id}
    )
    removed_sprint = authenticated_client.post(
        f"{project_url}/sprints/{sprint_id}/delete"
    )

    assert linked.status_code == 302
    assert removed_sprint.status_code == 302
    with app.app_context():
        story = db.session.get(UserStory, story_id)
        assert story is not None
        assert story.epic_id == epic_id
        assert story.sprint_backlog_id is None
        assert db.session.get(SprintBacklog, sprint_id) is None
        assert db.session.get(Project, project_id) is not None
