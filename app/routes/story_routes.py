from flask import Blueprint, flash, redirect, request, url_for
from flask_login import current_user, login_required

import app.services.epic_service as epic_srvc
import app.services.user_story_service as story_srvc
from app.services.exceptions import (
    ProjectDomainException,
    ServiceException,
    UserStoryDomainException,
)

story_bp = Blueprint("story", __name__)


@story_bp.route("/<int:project_id>/stories", methods=["POST"])
@login_required
def create_story(project_id: int):
    try:
        story_srvc.create_user_story(project_id, current_user.id, request.form)
        flash("História de usuário criada com sucesso!", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@story_bp.route("/<int:project_id>/stories/<int:story_id>/edit", methods=["POST"])
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


@story_bp.route("/<int:project_id>/stories/<int:story_id>/delete", methods=["POST"])
@login_required
def remove_story(project_id: int, story_id: int):
    try:
        story_srvc.delete_user_story(story_id, project_id, current_user.id)
        flash("História de usuário excluída com sucesso!", "success")
    except (ProjectDomainException, UserStoryDomainException) as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@story_bp.route("/<int:project_id>/epics", methods=["POST"])
@login_required
def create_epic(project_id: int):
    try:
        epic_srvc.create_epic(project_id, current_user.id, request.form.get("title"))
        flash("Épico criado com sucesso!", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@story_bp.route("/<int:project_id>/epics/<int:epic_id>/edit", methods=["POST"])
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


@story_bp.route("/<int:project_id>/epics/<int:epic_id>/delete", methods=["POST"])
@login_required
def remove_epic(project_id: int, epic_id: int):
    try:
        epic_srvc.delete_epic(epic_id, project_id, current_user.id)
        flash("Épico excluído com sucesso. As histórias foram mantidas.", "success")
    except ServiceException as error:
        flash(error.message, "danger")
    return redirect(url_for("projects.project_detail", project_id=project_id))


@story_bp.route("/<int:project_id>/epics/<int:epic_id>/stories/link", methods=["POST"])
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


@story_bp.route(
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
