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
    "competição criada para testar o raciocínio lógico e os conhecimentos em "
    "funções trigonométricas. A competição acontece em um grande centro de "
    "treinamento dividido em 5 áreas, e cada uma delas possui obstáculos e "
    "desafios matemáticos que devem ser resolvidos corretamente para liberar o "
    "acesso à próxima fase.\n\n"
    "No entanto, antes do início da competição, um ex-participante invadiu o "
    "sistema e bloqueou todas as fases. Agora, para avançar, será necessário "
    "recuperar os 5 códigos de acesso disponibilizados após os desafios.\n\n"
    "Seu objetivo é completar todas as fases, responder às perguntas sobre "
    "seno, cosseno, tangente, secante, cossecante e cotangente e desbloquear "
    "o sistema para concluir a competição.\n\n"
    "A cada fase, você enfrentará problemas que exigem atenção, lógica e "
    "domínio dos conceitos trigonométricos. Ao acertar os desafios, você ganha "
    "acesso ao próximo setor do centro de treinamento. Mas cuidado: o tempo e a "
    "precisão serão fundamentais.\n\n"
    "Caso o jogador tenha dificuldade, poderá receber auxílio com as dicas; "
    "porém, quanto mais dicas utilizar, menos pontos receberá. Ele terá até 3 "
    "chances de errar em cada etapa. Caso ultrapasse esse limite, precisará "
    "reiniciar o jogo e começar novamente.\n\n"
    "A missão final é recuperar todos os códigos, concluir as 5 áreas e provar "
    "que você domina as funções trigonométricas."
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
