# app/routes/project_routes.py
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

import app.services.project_service as srvc
from app.services.exceptions import ProjectDomainException

projects_bp = Blueprint("projects", __name__)


@projects_bp.route("/", methods=["GET"], strict_slashes=False)
@login_required
def projects_list():
    # US-005 Gerenciar projetos (LEITURA)
    projects = srvc.get_projects_by_user(current_user.id)
    return render_template("projects.html", projects=projects)


@projects_bp.route("/", methods=["POST"], strict_slashes=False)
@login_required
def create_project():
    """
    Rota para criar projeto, recebendo nome do projeto em formulário, e em
    caso de sucesso, redireciona para a página principal do projeto
    """
    name = request.form.get("name")

    try:
        new_project = srvc.create_project(user_id=current_user.id, name=name)
        flash("Projeto criado com sucesso!", "success")

        return redirect(url_for("projects.project_detail", project_id=new_project.id))

    except ProjectDomainException as error:
        flash(error.message, "danger")
        return redirect(url_for("projects.list_projects"))


@projects_bp.route("/<int:project_id>", methods=["GET"], strict_slashes=False)
@login_required
def project_detail(project_id: int):
    # Lógica para carregar e exibir os detalhes do projeto
    project = srvc.get_project_by_id(project_id, current_user.id)
    return render_template("project_detail.html", project=project)
