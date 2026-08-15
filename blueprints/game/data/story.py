"""Armazena os textos narrativos, mensagens e códigos recebidos na história."""

GAME_INFO = {
    "name": "Desafio Trigonométrico",
    "target_audience": "Estudantes do Ensino Médio e pessoas se preparando para vestibulares ou concursos.",
    "objective": "Recuperar os 5 códigos de acesso resolvendo desafios sobre funções trigonométricas.",
    "final_code": "VOCÊ DOMINOU AS FUNÇÕES TRIGONOMÉTRICAS",
    "rules": [
        "Cada exercício correto sem dicas vale 100 pontos.",
        "Com uma dica, a resposta correta vale 70 pontos.",
        "Com duas dicas, a resposta correta vale 50 pontos.",
        "Ao errar 3 perguntas, o jogador precisa reiniciar o jogo.",
        "A próxima fase é liberada ao acertar todos os desafios da fase atual.",
    ],
}

INTRODUCTION = (
    "Você foi selecionado para participar do Desafio Trigonométrico, uma "
    "competição criada para testar raciocínio lógico e conhecimentos em "
    "funções trigonométricas."
)

STAGE_STORIES = {
    1: {
        "intro": "Bem-vindo! Vamos começar pelos conceitos básicos. Resolva os desafios para continuar.",
        "success": "Parabéns! Você concluiu a primeira sala.",
    },
    2: {
        "intro": "A segunda sala exige conhecimentos sobre funções relativas.",
        "success": "Sala concluída com sucesso!",
    },
    3: {
        "intro": "Agora o desafio envolve propriedades das funções trigonométricas, como período.",
        "success": "Você está na metade do caminho.",
    },
    4: {
        "intro": "A penúltima sala exige concentração e relações entre funções trigonométricas.",
        "success": "Excelente! Continue para a fase final.",
    },
    5: {
        "intro": "Na sala final, aplique seus conhecimentos em situações reais do cotidiano.",
        "success": "Você chegou ao final do desafio!",
    },
}

CLASSIFICATIONS = [
    {"min_score": 0, "max_score": 500, "title": "Aprendiz Trigonométrico"},
    {"min_score": 501, "max_score": 699, "title": "Explorador Matemático"},
    {"min_score": 700, "max_score": 899, "title": "Especialista em Trigonometria"},
    {"min_score": 900, "max_score": 1000, "title": "Mestre das Funções Trigonométricas"},
]
