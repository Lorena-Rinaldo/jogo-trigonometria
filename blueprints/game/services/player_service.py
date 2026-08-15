"""Gerencia os dados do jogador e a escolha de personagem."""

from blueprints.game.data.characters import CHARACTERS
from blueprints.game.utils.helpers import find_character_by_id
from database.supabase_client import supabase


def normalize_player_name(player_name):
    """Normaliza o nome usado como chave de busca do jogador."""
    return player_name.strip().lower()


def format_player(row):
    """Formata o jogador salvo no banco para o formato usado pela API."""
    if not row:
        return None

    character = find_character_by_id(CHARACTERS, row["character_id"])
    return {
        "id": row["id"],
        "name": row["name"],
        "character": character,
    }


def get_characters():
    """Lista os personagens disponíveis para escolha."""
    return CHARACTERS


def create_player(player_name, character_id):
    """Cria ou atualiza um jogador com o personagem escolhido."""
    character = find_character_by_id(CHARACTERS, character_id)
    if not character:
        return {"error": "Personagem não encontrado."}, 404

    normalized_name = normalize_player_name(player_name)
    payload = {
        "normalized_name": normalized_name,
        "name": player_name.strip(),
        "character_id": character_id,
    }

    response = supabase.table("players").upsert(payload).execute()
    player = format_player(response.data[0])

    return {
        "message": "Jogador registrado com sucesso.",
        "player": player,
    }, 201


def get_player(player_name):
    """Busca um jogador pelo nome."""
    normalized_name = normalize_player_name(player_name)
    response = (
        supabase.table("players")
        .select("*")
        .eq("normalized_name", normalized_name)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return format_player(response.data[0])


def get_player_by_id(player_id):
    """Busca um jogador pelo ID."""
    response = (
        supabase.table("players")
        .select("*")
        .eq("id", player_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return format_player(response.data[0])


def get_or_create_default_player(player_name):
    """Cria um jogador padrão quando o front ainda não enviou personagem."""
    player = get_player(player_name)
    if player:
        return player

    create_player(player_name, CHARACTERS[0]["id"])
    return get_player(player_name)
