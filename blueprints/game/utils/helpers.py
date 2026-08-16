"""Reúne pequenas funções auxiliares usadas em outras partes do jogo."""

import unicodedata


def find_exercise_by_id(exercises, exercise_id):
    """Busca uma pergunta pelo ID."""
    return next(
        (exercise for exercise in exercises if exercise["id"] == exercise_id),
        None,
    )


def find_stage_by_id(stages, stage_id):
    """Busca uma fase pelo ID."""
    return next((stage for stage in stages if stage["id"] == stage_id), None)


def find_character_by_id(characters, character_id):
    """Busca um personagem pelo ID."""
    return next(
        (character for character in characters if character["id"] == character_id),
        None,
    )


def sanitize_exercise(exercise):
    """Remove dados sensíveis antes de enviar a pergunta ao frontend."""
    return {
        "id": exercise["id"],
        "stage_id": exercise["stage_id"],
        "question_number": exercise.get("question_number", ((exercise["id"] - 1) % 2) + 1),
        "instruction": exercise.get("instruction", ""),
        "question": exercise["question"],
        "options": exercise["options"],
        "hints_count": len(exercise["hints"]),
    }


def normalize_text(value):
    """Normaliza texto para comparações sem depender de acentos ou maiúsculas."""
    normalized = unicodedata.normalize("NFD", value.strip().lower())
    without_accents = "".join(
        character for character in normalized if unicodedata.category(character) != "Mn"
    )
    return " ".join(without_accents.split())
