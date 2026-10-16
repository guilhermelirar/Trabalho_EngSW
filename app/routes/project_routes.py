# app/routes/project_routes.py
from flask import Blueprint, render_template
from flask_login import login_required

projects_bp = Blueprint('projects', __name__)

# LOGIN
@projects_bp.route('/projects', methods=['GET'])
@login_required
def projects_list():
    # US-005 Gerenciar projetos (LEITURA)
    return render_template('projects.html')

