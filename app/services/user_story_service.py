from app.models import db
from app.models.acceptance_criteria import AcceptanceCriteria
from app.models.user_story import UserStory
from app.services import project_service
from app.services.exceptions import ProjectDomainException, UserStoryDomainException

STORY_POINT_VALUES = {0, 1, 2, 3, 5, 8, 13, 21, 34, 55}
MOSCOW_VALUES = {"M", "S", "C", "W"}
MOSCOW_ALIASES = {
    "M": "M",
    "MUST": "M",
    "S": "S",
    "SHOULD": "S",
    "C": "C",
    "COULD": "C",
    "W": "W",
    "WONT": "W",
    "WON'T": "W",
}
RICE_IMPACT_VALUES = {0.25, 0.5, 1, 2, 3}
RICE_CONFIDENCE_VALUES = {50, 80, 100}


def validate_user_story_data(data: dict, require_all: bool = True) -> None:
    required_fields = ["title", "role", "action", "benefit"]
    for field in required_fields:
        val = data.get(field)
        if (not val and require_all) or not str(val).strip():
            raise UserStoryDomainException(f"O campo '{field}' é obrigatório.")


def _optional_number(value, field: str, parser):
    if value is None or not str(value).strip():
        return None
    try:
        return parser(str(value))
    except ValueError as error:
        raise UserStoryDomainException(
            f"O campo '{field}' possui um valor inválido."
        ) from error


def get_prioritization_data(data: dict) -> dict:
    """Valida e normaliza os campos de estimativa e priorização da HU."""
    story_points = _optional_number(data.get("story_points"), "Story Points", int)
    if story_points is not None and story_points not in STORY_POINT_VALUES:
        raise UserStoryDomainException("Selecione um valor de Story Points permitido.")

    moscow = data.get("moscow")
    moscow = MOSCOW_ALIASES.get(str(moscow).strip().upper()) if moscow else None
    if data.get("moscow") and moscow is None:
        raise UserStoryDomainException("Selecione uma classificação MoSCoW válida.")
    if moscow is not None and moscow not in MOSCOW_VALUES:
        raise UserStoryDomainException("Selecione uma classificação MoSCoW válida.")

    reach = _optional_number(data.get("rice_reach"), "Alcance", int)
    impact = _optional_number(data.get("rice_impact"), "Impacto", float)
    confidence = _optional_number(data.get("rice_confidence"), "Confiança", int)

    if reach is not None and reach < 0:
        raise UserStoryDomainException("O Alcance não pode ser negativo.")
    if impact is not None and impact not in RICE_IMPACT_VALUES:
        raise UserStoryDomainException("Selecione um valor de Impacto permitido.")
    if confidence is not None and confidence not in RICE_CONFIDENCE_VALUES:
        raise UserStoryDomainException("Selecione um valor de Confiança permitido.")

    return {
        "story_points": story_points,
        "moscow": moscow,
        "rice_reach": reach,
        "rice_impact": impact,
        "rice_confidence": confidence,
    }


def create_user_story(project_id: int, user_id: int, data: dict) -> UserStory:
    """
    Cria uma história de usuário associada a um projeto
    """
    # Valida se projeto pertence ao usuário
    project = project_service.get_project_by_id(project_id, user_id)
    if not project:
        raise ProjectDomainException("Projeto não encontrado", status_code=404)
    if not project.backlog:
        raise ProjectDomainException(
            "O projeto não possui um Product Backlog.", status_code=404
        )

    validate_user_story_data(data, require_all=True)

    sprint_id = data.get("sprint_backlog_id")
    sprint_backlog_id = int(sprint_id) if sprint_id and sprint_id.strip() else None

    user_story = UserStory()
    user_story.project_backlog_id = project.backlog.id
    user_story.title = str(data["title"]).strip()
    user_story.role = str(data["role"]).strip()
    user_story.action = str(data["action"]).strip()
    user_story.benefit = str(data["benefit"]).strip()

    # Valida se sprint pertence ao projeto
    if sprint_backlog_id:
        valid_sprint_ids = {sprint.id for sprint in project.backlog.sprints}
        if sprint_backlog_id not in valid_sprint_ids:
            raise UserStoryDomainException("Sprint inválida para este projeto.")
        user_story.sprint_backlog_id = sprint_backlog_id

    prioritization_data = get_prioritization_data(data)
    for field, value in prioritization_data.items():
        setattr(user_story, field, value)

    db.session.add(user_story)
    db.session.commit()
    return user_story


def get_user_story(story_id: int, user_id: int):
    story = db.session.get(UserStory, story_id)
    if not story or story.project_backlog.project.owner_id != user_id:
        raise UserStoryDomainException(
            "História de usuário não encontrada", status_code=404
        )

    return story


def update_user_story(story_id: int, user_id: int, new_data: dict) -> UserStory:
    """
    Edita campos de uma história de usuário existente.
    """
    # busca história de usuário no banco de dados
    story = db.session.get(UserStory, story_id)
    if not story:
        raise UserStoryDomainException(
            "História de usuário não encontrada.", status_code=404
        )

    if not project_service.get_project_by_id(story.project_backlog.project_id, user_id):
        raise ProjectDomainException("Projeto não encontrado", status_code=404)

    validate_user_story_data(new_data, require_all=False)

    if new_data.get("title"):
        story.title = str(new_data["title"]).strip()
    if new_data.get("role"):
        story.role = str(new_data["role"]).strip()
    if new_data.get("action"):
        story.action = str(new_data["action"]).strip()
    if new_data.get("benefit"):
        story.benefit = str(new_data["benefit"]).strip()

    if "sprint_backlog_id" in new_data:
        raw_sprint_id = new_data.get("sprint_backlog_id")
        story.sprint_backlog_id = (
            int(raw_sprint_id) if raw_sprint_id and str(raw_sprint_id).strip() else None
        )

    prioritization_fields = {
        "story_points",
        "moscow",
        "rice_reach",
        "rice_impact",
        "rice_confidence",
    }
    if any(field in new_data for field in prioritization_fields):
        prioritization_data = get_prioritization_data(new_data)
        for field, value in prioritization_data.items():
            setattr(story, field, value)

    db.session.commit()
    return story


def delete_user_story(story_id: int, user_id: int):
    """
    Deleta uma história de usuário se encontrar
    """
    story = get_user_story(story_id, user_id)
    db.session.delete(story)
    db.session.commit()


def _validate_acceptance_criteria_data(data: dict, require_all: bool = True) -> dict:
    """
    Sanitiza e valida os dados do formulário de Critérios de Aceitação.
    Retorna os campos limpos se válidos ou levanta UserStoryDomainException.
    """
    if not data:
        raise UserStoryDomainException(
            "Os dados do critério de aceitação não podem estar vazios."
        )

    title = (data.get("title") or "").strip()
    given = (data.get("given") or "").strip()
    when = (data.get("when") or "").strip()
    then = (data.get("then") or "").strip()

    cleaned_fields = {
        "title": title,
        "given": given,
        "when": when,
        "then": then,
    }

    if require_all:
        missing = [
            field_name for field_name, value in cleaned_fields.items() if not value
        ]
        if missing:
            raise UserStoryDomainException(
                "Todos os campos do critério de aceitação (Título, Dado, Quando, Então) são obrigatórios."
            )

    return cleaned_fields


def add_acceptance_criteria_to_story(
    story_id: int, user_id: int, data: dict
) -> AcceptanceCriteria:
    """
    Cria um objeto AcceptanceCriteria a partir de data, e vincula a uma história
    de usuário existente. Retorna o objeto criado em caso de sucesso, e levanta
    UserStoryDomainException em caso de erro.
    """

    # Validação de permissão do usuário e dos campos de critério de aceitação
    story = get_user_story(story_id, user_id)
    cleaned_data = _validate_acceptance_criteria_data(data, require_all=True)

    # Criando objeto e adicionando no banco de dados
    criteria = AcceptanceCriteria()
    criteria.user_story_id = story.id
    criteria.title = cleaned_data["title"]
    criteria.given = cleaned_data["given"]
    criteria.when = cleaned_data["when"]
    criteria.then = cleaned_data["then"]

    db.session.add(criteria)
    db.session.commit()

    return criteria
