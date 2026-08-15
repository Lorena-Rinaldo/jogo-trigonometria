"""Define validações para cadastro e escolha de personagem do jogador."""


def validate_player_payload(payload):
    """Valida os dados enviados para criar ou atualizar um jogador."""
    errors = []

    if not isinstance(payload.get("player_name"), str) or not payload.get("player_name").strip():
        errors.append("player_name é obrigatório e deve ser texto.")

    if not isinstance(payload.get("character_id"), int):
        errors.append("character_id é obrigatório e deve ser número inteiro.")

    return errors
