# tests/test_project_routes.py

from flask.testing import FlaskClient


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
