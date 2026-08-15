"""Coordena as regras gerais do jogo."""

from blueprints.game.data.exercises import EXERCISES
from blueprints.game.data.stages import STAGES
from blueprints.game.data.story import GAME_INFO, INTRODUCTION, STAGE_STORIES
from blueprints.game.services.progress_service import (
    add_correct_answer,
    add_hint_usage,
    add_wrong_answer,
    get_or_create_progress,
    reset_progress,
    validate_final_code_for_player,
)
from blueprints.game.services.player_service import get_player, get_player_by_id
from blueprints.game.services.score_service import calculate_question_points, get_classification
from blueprints.game.utils.helpers import (
    find_exercise_by_id,
    find_stage_by_id,
    normalize_text,
    sanitize_exercise,
)


def get_game_overview():
    """Retorna informações gerais do jogo."""
    return {
        **GAME_INFO,
        "introduction": INTRODUCTION,
        "total_stages": len(STAGES),
        "total_questions": len(EXERCISES),
    }


def get_stages():
    """Lista as fases com dados resumidos."""
    return [
        {
            **stage,
            "intro": STAGE_STORIES[stage["id"]]["intro"],
            "questions_count": len(
                [exercise for exercise in EXERCISES if exercise["stage_id"] == stage["id"]]
            ),
        }
        for stage in STAGES
    ]


def get_stage(stage_id):
    """Retorna uma fase específica com perguntas sem resposta correta."""
    stage = find_stage_by_id(STAGES, stage_id)
    if not stage:
        return None

    exercises = [
        sanitize_exercise(exercise)
        for exercise in EXERCISES
        if exercise["stage_id"] == stage_id
    ]

    return {
        **stage,
        "intro": STAGE_STORIES[stage_id]["intro"],
        "success_message": STAGE_STORIES[stage_id]["success"],
        "exercises": exercises,
    }


def use_hint(player_name, question_id):
    """Libera uma dica para uma pergunta."""
    exercise = find_exercise_by_id(EXERCISES, question_id)
    if not exercise:
        return {"error": "Pergunta não encontrada."}, 404

    progress = get_or_create_progress(player_name)
    if exercise["stage_id"] > progress["current_stage"]:
        return {"error": "Esta fase ainda não foi liberada."}, 403

    question_key = str(question_id)
    used_hints = progress["hints_used"].get(question_key, 0)

    if used_hints >= len(exercise["hints"]):
        return {
            "message": "Todas as dicas desta pergunta já foram usadas.",
            "hints_used": used_hints,
        }, 200

    add_hint_usage(player_name, question_id)
    progress = get_or_create_progress(player_name)
    hint_index = progress["hints_used"][question_key] - 1

    return {
        "question_id": question_id,
        "hint": exercise["hints"][hint_index],
        "hints_used": progress["hints_used"][question_key],
    }, 200


def answer_question(player_name, question_id, selected_option):
    """Verifica resposta, pontua e atualiza progresso."""
    exercise = find_exercise_by_id(EXERCISES, question_id)
    if not exercise:
        return {"error": "Pergunta não encontrada."}, 404

    progress = get_or_create_progress(player_name)

    if progress["game_over"]:
        return {
            "message": "O jogo foi encerrado por limite de erros. Reinicie para jogar novamente.",
            "progress": progress,
        }, 200

    if exercise["stage_id"] > progress["current_stage"]:
        return {
            "error": "Esta fase ainda não foi liberada.",
            "current_stage": progress["current_stage"],
        }, 403

    if question_id in progress["answered_questions"]:
        return {
            "message": "Esta pergunta já foi respondida corretamente.",
            "progress": progress,
        }, 200

    is_correct = selected_option.lower().strip() == exercise["correct_option"]

    if not is_correct:
        progress = add_wrong_answer(player_name)
        return {
            "correct": False,
            "message": "Resposta incorreta. Tente novamente.",
            "remaining_errors": max(0, 3 - progress["wrong_answers"]),
            "progress": progress,
        }, 200

    hints_used = progress["hints_used"].get(str(question_id), 0)
    points = calculate_question_points(hints_used)
    completed_stages_before = set(progress["completed_stages"])
    progress = add_correct_answer(player_name, exercise, points)
    completed_stages_after = set(progress["completed_stages"])
    stage_completed = exercise["stage_id"] in completed_stages_after - completed_stages_before
    completed_stage = find_stage_by_id(STAGES, exercise["stage_id"])

    return {
        "correct": True,
        "message": "Resposta correta!",
        "earned_points": points,
        "answer": exercise["answer"],
        "stage_completed": stage_completed,
        "completed_stage": exercise["stage_id"] if stage_completed else None,
        "code_received": completed_stage["code"] if stage_completed else None,
        "next_stage": progress["current_stage"] if stage_completed and not progress["awaiting_final_code"] else None,
        "awaiting_final_code": progress["awaiting_final_code"],
        "all_stages_completed": progress["awaiting_final_code"] or progress["completed"],
        "progress": progress,
    }, 200


def get_player_progress(player_name):
    """Consulta o progresso atual do jogador."""
    progress = get_or_create_progress(player_name)
    player = get_player(player_name)

    if player:
        progress["player_name"] = player["name"]
        progress["character"] = player["character"]

    return {
        **progress,
        "classification": get_classification(progress["score"]),
    }


def restart_player(player_name):
    """Reinicia o progresso do jogador."""
    progress = reset_progress(player_name)
    return {
        "message": "Progresso reiniciado.",
        "progress": progress,
    }


def restart_player_by_id(player_id):
    """Reinicia o progresso do jogador pelo ID."""
    player = get_player_by_id(player_id)
    if not player:
        return {"error": "Jogador não encontrado."}, 404

    progress = reset_progress(player["name"])
    return {
        "message": "Progresso reiniciado.",
        "progress": progress,
    }, 200


def validate_final_code(player_name, code):
    """Valida o código final digitado pelo jogador."""
    progress = get_or_create_progress(player_name)

    if progress["game_over"]:
        return {
            "error": "O jogo foi encerrado por limite de erros. Reinicie para jogar novamente.",
            "progress": progress,
        }, 403

    if len(progress["completed_stages"]) < len(STAGES):
        return {
            "error": "Você ainda não concluiu todas as fases.",
            "progress": progress,
        }, 403

    expected_code = GAME_INFO["final_code"]
    if normalize_text(code) != normalize_text(expected_code):
        return {
            "valid": False,
            "message": "Código final incorreto. Confira os códigos recebidos nas fases.",
            "expected_order": progress["unlocked_codes"],
            "progress": progress,
        }, 200

    progress = validate_final_code_for_player(player_name)
    return {
        "valid": True,
        "message": "Código final correto! Desafio concluído.",
        "final_code": expected_code,
        "progress": progress,
    }, 200


def get_certificate(player_name):
    """Retorna certificado quando o jogo foi concluído."""
    progress = get_or_create_progress(player_name)

    if not progress["completed"]:
        return {
            "error": "Certificado indisponível. Conclua todas as fases e valide o código final primeiro.",
            "progress": progress,
        }, 403

    return {
        "certificate": {
            "player_name": progress["player_name"],
            "title": get_classification(progress["score"]),
            "score": progress["score"],
            "message": "Parabéns! Você concluiu o Desafio Trigonométrico com sucesso.",
            "final_code": GAME_INFO["final_code"],
        }
    }, 200


def get_certificate_by_id(player_id):
    """Retorna certificado pelo ID do jogador."""
    player = get_player_by_id(player_id)
    if not player:
        return {"error": "Jogador não encontrado."}, 404

    result, status_code = get_certificate(player["name"])
    if status_code == 200:
        result["certificate"]["player_id"] = player_id

    return result, status_code
