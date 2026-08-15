"""Armazena as perguntas, alternativas, respostas corretas e dicas do jogo."""

EXERCISES = [
    {
        "id": 1,
        "stage_id": 1,
        "question": "Qual é o valor de sen(30°)?",
        "options": [
            {"id": "a", "text": "0"},
            {"id": "b", "text": "1/2"},
            {"id": "c", "text": "raiz de 3 / 2"},
            {"id": "d", "text": "1"},
        ],
        "correct_option": "b",
        "answer": "1/2",
        "hints": [
            "Lembre-se dos valores do triângulo notável de 30, 60 e 90°.",
            "No círculo trigonométrico, o seno de 30° vale metade da unidade.",
        ],
    },
    {
        "id": 2,
        "stage_id": 1,
        "question": "Qual é o valor de cos(60°)?",
        "options": [
            {"id": "a", "text": "1/2"},
            {"id": "b", "text": "0"},
            {"id": "c", "text": "raiz de 3 / 2"},
            {"id": "d", "text": "1"},
        ],
        "correct_option": "a",
        "answer": "1/2",
        "hints": [
            "Compare o cosseno de 60° com o seno de 30°.",
            "O valor de cos(60°) é igual ao sen(30°).",
        ],
    },
    {
        "id": 3,
        "stage_id": 2,
        "question": "A secante é o inverso de qual função?",
        "options": [
            {"id": "a", "text": "seno"},
            {"id": "b", "text": "cosseno"},
            {"id": "c", "text": "tangente"},
            {"id": "d", "text": "cossecante"},
        ],
        "correct_option": "b",
        "answer": "cosseno",
        "hints": [
            "Pense nas funções recíprocas.",
            "A secante é calculada por sec(x) = 1 / cos(x).",
        ],
    },
    {
        "id": 4,
        "stage_id": 2,
        "question": "Qual é o valor de cossec(30°)?",
        "options": [
            {"id": "a", "text": "raiz de 3"},
            {"id": "b", "text": "2"},
            {"id": "c", "text": "1"},
            {"id": "d", "text": "1/2"},
        ],
        "correct_option": "b",
        "answer": "2",
        "hints": [
            "Primeiro descubra o valor de sen(30°).",
            "A cossecante é o inverso do seno: cossec(x) = 1 / sen(x).",
        ],
    },
    {
        "id": 5,
        "stage_id": 3,
        "question": "Qual é o período da função sen(x)?",
        "options": [
            {"id": "a", "text": "pi"},
            {"id": "b", "text": "2pi"},
            {"id": "c", "text": "4pi"},
            {"id": "d", "text": "pi/2"},
        ],
        "correct_option": "b",
        "answer": "2pi",
        "hints": [
            "Pense em quanto o gráfico precisa avançar para se repetir.",
            "A função seno completa um ciclo a cada 360°.",
        ],
    },
    {
        "id": 6,
        "stage_id": 3,
        "question": "Qual é o valor da cotg(45°)?",
        "options": [
            {"id": "a", "text": "1"},
            {"id": "b", "text": "0"},
            {"id": "c", "text": "raiz de 3"},
            {"id": "d", "text": "2"},
        ],
        "correct_option": "a",
        "answer": "1",
        "hints": [
            "Lembre-se do valor de tg(45°).",
            "A cotangente é o inverso da tangente: cotg(x) = 1 / tg(x).",
        ],
    },
    {
        "id": 7,
        "stage_id": 4,
        "question": "Sabendo que sen(x) = 1/2, com x no primeiro quadrante, qual é o valor de cossec(x)?",
        "options": [
            {"id": "a", "text": "1/2"},
            {"id": "b", "text": "raiz de 3"},
            {"id": "c", "text": "2"},
            {"id": "d", "text": "raiz de 2"},
        ],
        "correct_option": "c",
        "answer": "2",
        "hints": [
            "A cossecante depende diretamente do seno.",
            "Use cossec(x) = 1 / sen(x).",
        ],
    },
    {
        "id": 8,
        "stage_id": 4,
        "question": "Sabendo que tg(x) = 1, e que x pertence ao primeiro quadrante, qual é o valor de cotg(x)?",
        "options": [
            {"id": "a", "text": "0"},
            {"id": "b", "text": "raiz de 3"},
            {"id": "c", "text": "1"},
            {"id": "d", "text": "2"},
        ],
        "correct_option": "c",
        "answer": "1",
        "hints": [
            "A cotangente é a função recíproca da tangente.",
            "Se tg(x) = 1, então cotg(x) = 1 / 1.",
        ],
    },
    {
        "id": 9,
        "stage_id": 5,
        "question": "Uma rampa forma 30° com o solo e tem 8 metros de comprimento. Qual altura ela alcança? Considere sen(30°) = 0,5.",
        "options": [
            {"id": "a", "text": "2 m"},
            {"id": "b", "text": "4 m"},
            {"id": "c", "text": "6 m"},
            {"id": "d", "text": "8 m"},
        ],
        "correct_option": "b",
        "answer": "4 m",
        "hints": [
            "Desenhe um triângulo retângulo e identifique a hipotenusa e a altura.",
            "Use sen(x) = cateto oposto / hipotenusa.",
        ],
    },
    {
        "id": 10,
        "stage_id": 5,
        "question": "Uma escada de 10 metros está apoiada em uma parede, formando 60° com o chão. Qual altura aproximada ela alcança? Considere sen(60°) = 0,866.",
        "options": [
            {"id": "a", "text": "5,05 m"},
            {"id": "b", "text": "7 m"},
            {"id": "c", "text": "8,66 m"},
            {"id": "d", "text": "10,17 m"},
        ],
        "correct_option": "c",
        "answer": "8,66 m",
        "hints": [
            "A escada representa a hipotenusa do triângulo.",
            "A altura corresponde ao cateto oposto.",
        ],
    },
]
