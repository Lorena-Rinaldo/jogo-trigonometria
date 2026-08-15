"""Calcula pontuação, penalidades por dicas e classificação final."""

from blueprints.game.data.story import CLASSIFICATIONS


def calculate_question_points(hints_used):
    """Calcula pontos de acordo com a quantidade de dicas usadas."""
    if hints_used <= 0:
        return 100

    if hints_used == 1:
        return 70

    return 50


def get_classification(score):
    """Retorna a classificação do jogador pela pontuação."""
    for classification in CLASSIFICATIONS:
        if classification["min_score"] <= score <= classification["max_score"]:
            return classification["title"]

    return CLASSIFICATIONS[-1]["title"]
