"""Define validações para cadastro e escolha de personagem do jogador."""

import re


PLAYER_NAME_PATTERN = re.compile(r"[A-Za-z]+(?: [A-Za-z]+)*")


def validate_player_payload(payload):
    """Valida os dados enviados para criar ou atualizar um jogador."""
    errors = []

    player_name = payload.get("player_name")
    if not isinstance(player_name, str) or not player_name.strip():
        errors.append("player_name é obrigatório e deve ser texto.")
    elif not PLAYER_NAME_PATTERN.fullmatch(player_name.strip()):
        errors.append("player_name deve conter apenas letras e espaços entre palavras.")

    if not isinstance(payload.get("character_id"), int):
        errors.append("character_id é obrigatório e deve ser número inteiro.")

    return errors
