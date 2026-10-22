# app/routes/project_routes.py
from flask import Blueprint, render_template, session
from flask_login import login_required
import app.services.project_service as srvc

projects_bp = Blueprint('projects', __name__)

# LOGIN
@projects_bp.route('/', methods=['GET'], strict_slashes=False)
@login_required
def projects_list():
    # US-005 Gerenciar projetos (LEITURA)
    user_id: int = session.get('_user_id', 0)

    projects = srvc.get_projects_by_user(user_id) 
    return render_template('projects.html', projects=projects)


