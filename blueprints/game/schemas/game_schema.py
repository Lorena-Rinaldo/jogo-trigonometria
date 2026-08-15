"""Define validações simples para entrada de dados da API do jogo."""


def validate_answer_payload(payload):
    """Valida os dados enviados ao responder uma pergunta."""
    errors = []

    if not isinstance(payload.get("player_name"), str) or not payload.get("player_name").strip():
        errors.append("player_name é obrigatório e deve ser texto.")

    if not isinstance(payload.get("question_id"), int):
        errors.append("question_id é obrigatório e deve ser número inteiro.")

    if not isinstance(payload.get("selected_option"), str) or not payload.get("selected_option").strip():
        errors.append("selected_option é obrigatório e deve ser texto.")

    return errors


def validate_hint_payload(payload):
    """Valida os dados enviados ao solicitar uma dica."""
    errors = []

    if not isinstance(payload.get("player_name"), str) or not payload.get("player_name").strip():
        errors.append("player_name é obrigatório e deve ser texto.")

    if not isinstance(payload.get("question_id"), int):
        errors.append("question_id é obrigatório e deve ser número inteiro.")

    return errors


def validate_restart_payload(payload):
    """Valida os dados enviados ao reiniciar um jogador."""
    errors = []

    if not isinstance(payload.get("player_name"), str) or not payload.get("player_name").strip():
        errors.append("player_name é obrigatório e deve ser texto.")

    return errors


def validate_final_code_payload(payload):
    """Valida os dados enviados ao confirmar o código final."""
    errors = []

    if not isinstance(payload.get("player_name"), str) or not payload.get("player_name").strip():
        errors.append("player_name é obrigatório e deve ser texto.")

    if not isinstance(payload.get("code"), str) or not payload.get("code").strip():
        errors.append("code é obrigatório e deve ser texto.")

    return errors
