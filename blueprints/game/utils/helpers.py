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
    """
    Remove dados sensíveis (como a resposta correta direta) 
    antes de enviar ao frontend, mas mantém as opções e feedbacks.
    """

    sanitized_options = [
        {
            "id": opt["id"],
            "text": opt["text"],
            "feedback": opt["feedback"] # O feedback agora vai para o front
        } for opt in exercise["options"]
    ]

    return {
        "id": exercise["id"],
        "stage_id": exercise["stage_id"],
        "question_number": exercise.get("question_number", ((exercise["id"] - 1) % 2) + 1),
        "instruction": exercise.get("instruction", ""),
        "question": exercise["question"],
        "options": sanitized_options,
        "hints_count": len(exercise["hints"]),
    }

def check_answer(exercise, selected_option_id):
    """
    Valida a opção escolhida e retorna o feedback específico.
    Retorna um dicionário com: is_correct (bool) e message (str).
    """
    is_correct = exercise["correct_option"] == selected_option_id
    
    selected_option = next(
        (opt for opt in exercise["options"] if opt["id"] == selected_option_id),
        None
    )
    
    message = selected_option["feedback"] if selected_option else "Opção inválida."
    
    return {
        "is_correct": is_correct,
        "message": message
    }

def normalize_text(value):
    """Normaliza texto para comparações sem depender de acentos ou maiúsculas."""
    normalized = unicodedata.normalize("NFD", value.strip().lower())
    without_accents = "".join(
        character for character in normalized if unicodedata.category(character) != "Mn"
    )
    return " ".join(without_accents.split())