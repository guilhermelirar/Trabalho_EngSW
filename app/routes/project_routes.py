# app/routes/project_routes.py
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

import app.services.project_service as srvc
import app.services.epic_service as epic_srvc
import app.services.user_story_service as story_srvc
from app.services.exceptions import (
    ProjectDomainException,
    ServiceException,
    UserStoryDomainException,
)

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
        return redirect(url_for("projects.projects_list"))


@projects_bp.route("/<int:project_id>", methods=["GET"], strict_slashes=False)
@login_required
def project_detail(project_id: int):
    # Lógica para carregar e exibir os detalhes do projeto
    try:
        project = srvc.get_project_by_id(project_id, current_user.id)
    except ProjectDomainException as error:
        abort(error.status_code)
    return render_template("project_detail.html", project=project)


@projects_bp.route("/<int:project_id>/edit", methods=["POST"])
@login_required
def update_project(project_id: int):
    try:
        srvc.update_project(project_id, current_user.id, request.form.get("name"))
        flash("Projeto atualizado com sucesso!", "success")
    except ProjectDomainException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.projects_list"))


@projects_bp.route("/<int:project_id>/delete", methods=["POST"])
@login_required
def remove_project(project_id: int):
    try:
        srvc.delete_project(project_id, current_user.id)
        flash("Projeto excluído com sucesso!", "success")
    except ProjectDomainException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.projects_list"))


@projects_bp.route("/<int:project_id>/backlog", methods=["POST"])
@login_required
def create_backlog(project_id: int):
    try:
        srvc.create_product_backlog(project_id, current_user.id)
        flash("Product Backlog criado com sucesso!", "success")
    except ProjectDomainException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/sprints", methods=["POST"])
@login_required
def create_sprint(project_id: int):
    try:
        project = srvc.get_project_by_id(project_id, current_user.id)
        if not project.backlog:
            raise ProjectDomainException("Crie o Product Backlog antes de adicionar uma sprint.")

        sprint_number = max(
            (sprint.sprint_number for sprint in project.backlog.sprints), default=0
        ) + 1
        srvc.create_sprint_backlog(current_user.id, project_id, sprint_number)
        flash(f"Sprint Backlog {sprint_number} criado com sucesso!", "success")
    except ProjectDomainException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/sprints/<int:sprint_id>/delete", methods=["POST"])
@login_required
def remove_sprint(project_id: int, sprint_id: int):
    try:
        srvc.delete_sprint_backlog(current_user.id, project_id, sprint_id)
        flash("Sprint Backlog removido. As histórias voltaram ao Product Backlog.", "success")
    except ProjectDomainException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/stories", methods=["POST"])
@login_required
def create_story(project_id: int):
    try:
        story_srvc.create_user_story(project_id, current_user.id, request.form)
        flash("História de usuário criada com sucesso!", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/stories/<int:story_id>/edit", methods=["POST"])
@login_required
def update_story(project_id: int, story_id: int):
    try:
        # Confirma a associação da história ao projeto antes da atualização.
        story_srvc.get_user_story(story_id, project_id, current_user.id)
        story_srvc.update_user_story(story_id, current_user.id, request.form)
        flash("História de usuário atualizada com sucesso!", "success")
    except (ProjectDomainException, UserStoryDomainException) as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/stories/<int:story_id>/delete", methods=["POST"])
@login_required
def remove_story(project_id: int, story_id: int):
    try:
        story_srvc.delete_user_story(story_id, project_id, current_user.id)
        flash("História de usuário excluída com sucesso!", "success")
    except (ProjectDomainException, UserStoryDomainException) as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/epics", methods=["POST"])
@login_required
def create_epic(project_id: int):
    try:
        epic_srvc.create_epic(project_id, current_user.id, request.form.get("title"))
        flash("Épico criado com sucesso!", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/epics/<int:epic_id>/edit", methods=["POST"])
@login_required
def update_epic(project_id: int, epic_id: int):
    try:
        epic_srvc.update_epic(
            epic_id, project_id, current_user.id, request.form.get("title")
        )
        flash("Épico atualizado com sucesso!", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route("/<int:project_id>/epics/<int:epic_id>/delete", methods=["POST"])
@login_required
def remove_epic(project_id: int, epic_id: int):
    try:
        epic_srvc.delete_epic(epic_id, project_id, current_user.id)
        flash("Épico excluído com sucesso. As histórias foram mantidas.", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route(
    "/<int:project_id>/epics/<int:epic_id>/stories/link", methods=["POST"]
)
@login_required
def link_story_to_epic(project_id: int, epic_id: int):
    try:
        story_id = int(request.form.get("story_id", ""))
        epic_srvc.link_user_story(epic_id, story_id, project_id, current_user.id)
        flash("História de usuário vinculada ao épico!", "success")
    except (TypeError, ValueError):
        flash("Selecione uma história de usuário válida.", "danger")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@projects_bp.route(
    "/<int:project_id>/epics/<int:epic_id>/stories/<int:story_id>/unlink",
    methods=["POST"],
)
@login_required
def unlink_story_from_epic(project_id: int, epic_id: int, story_id: int):
    try:
        epic_srvc.unlink_user_story(epic_id, story_id, project_id, current_user.id)
        flash("História de usuário desvinculada do épico.", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))
