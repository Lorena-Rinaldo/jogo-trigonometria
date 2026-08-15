"""Controla progresso, fase atual, erros e tentativas do jogador."""

from blueprints.game.data.exercises import EXERCISES
from blueprints.game.data.stages import STAGES
from blueprints.game.services.player_service import (
    get_or_create_default_player,
    normalize_player_name,
)
from database.supabase_client import supabase


def create_initial_progress(player_name):
    """Cria o progresso inicial de um jogador."""
    player = get_or_create_default_player(player_name)

    return {
        "player_name": player["name"],
        "character": player["character"],
        "current_stage": 1,
        "score": 0,
        "wrong_answers": 0,
        "answered_questions": [],
        "completed_stages": [],
        "unlocked_codes": [],
        "hints_used": {},
        "awaiting_final_code": False,
        "final_code_validated": False,
        "completed": False,
        "game_over": False,
    }


def format_progress(row, player):
    """Formata o progresso salvo no banco para o formato usado pela API."""
    return {
        "player_name": player["name"],
        "character": player["character"],
        "current_stage": row["current_stage"],
        "score": row["score"],
        "wrong_answers": row["wrong_answers"],
        "answered_questions": row["answered_questions"] or [],
        "completed_stages": row["completed_stages"] or [],
        "unlocked_codes": row["unlocked_codes"] or [],
        "hints_used": row["hints_used"] or {},
        "awaiting_final_code": row["awaiting_final_code"],
        "final_code_validated": row["final_code_validated"],
        "completed": row["completed"],
        "game_over": row["game_over"],
    }


def progress_to_row(player_name, progress):
    """Converte o progresso da API para o formato da tabela player_progress."""
    return {
        "normalized_name": normalize_player_name(player_name),
        "current_stage": progress["current_stage"],
        "score": progress["score"],
        "wrong_answers": progress["wrong_answers"],
        "answered_questions": progress["answered_questions"],
        "completed_stages": progress["completed_stages"],
        "unlocked_codes": progress["unlocked_codes"],
        "hints_used": progress["hints_used"],
        "awaiting_final_code": progress["awaiting_final_code"],
        "final_code_validated": progress["final_code_validated"],
        "completed": progress["completed"],
        "game_over": progress["game_over"],
    }


def save_progress(player_name, progress):
    """Salva o progresso atual no Supabase."""
    supabase.table("player_progress").upsert(progress_to_row(player_name, progress)).execute()
    return get_or_create_progress(player_name)


def get_or_create_progress(player_name):
    """Busca ou cria o progresso do jogador no Supabase."""
    player = get_or_create_default_player(player_name)
    normalized_name = normalize_player_name(player_name)
    response = (
        supabase.table("player_progress")
        .select("*")
        .eq("normalized_name", normalized_name)
        .limit(1)
        .execute()
    )

    if response.data:
        return format_progress(response.data[0], player)

    progress = create_initial_progress(player_name)
    supabase.table("player_progress").insert(progress_to_row(player_name, progress)).execute()
    return progress


def reset_progress(player_name):
    """Reinicia o progresso de um jogador."""
    progress = create_initial_progress(player_name)
    return save_progress(player_name, progress)


def add_hint_usage(player_name, question_id):
    """Registra uso de dica em uma pergunta."""
    progress = get_or_create_progress(player_name)
    question_key = str(question_id)
    progress["hints_used"][question_key] = progress["hints_used"].get(question_key, 0) + 1
    return save_progress(player_name, progress)


def add_wrong_answer(player_name):
    """Registra uma resposta incorreta."""
    progress = get_or_create_progress(player_name)
    progress["wrong_answers"] += 1

    if progress["wrong_answers"] >= 3:
        progress["game_over"] = True

    return save_progress(player_name, progress)


def add_correct_answer(player_name, exercise, points):
    """Registra acerto, soma pontos e atualiza fase."""
    progress = get_or_create_progress(player_name)
    question_id = exercise["id"]

    if question_id not in progress["answered_questions"]:
        progress["answered_questions"].append(question_id)
        progress["score"] += points

    update_stage_progress(progress, exercise["stage_id"])
    return save_progress(player_name, progress)


def update_stage_progress(progress, stage_id):
    """Libera a próxima fase quando todas as perguntas da fase forem acertadas."""
    stage_questions = [
        exercise["id"] for exercise in EXERCISES if exercise["stage_id"] == stage_id
    ]

    stage_completed = all(
        question_id in progress["answered_questions"] for question_id in stage_questions
    )

    if not stage_completed:
        return

    if stage_id not in progress["completed_stages"]:
        progress["completed_stages"].append(stage_id)

    stage = next(stage for stage in STAGES if stage["id"] == stage_id)
    if stage["code"] not in progress["unlocked_codes"]:
        progress["unlocked_codes"].append(stage["code"])

    if stage_id < len(STAGES):
        progress["current_stage"] = stage_id + 1
    else:
        progress["awaiting_final_code"] = True


def validate_final_code_for_player(player_name):
    """Marca o código final como validado e conclui o jogo."""
    progress = get_or_create_progress(player_name)
    progress["awaiting_final_code"] = False
    progress["final_code_validated"] = True
    progress["completed"] = True
    return save_progress(player_name, progress)
