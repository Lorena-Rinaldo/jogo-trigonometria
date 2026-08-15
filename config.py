"""Guarda as configurações globais da aplicação."""


class Config:
    """Configurações principais do backend."""

    DEBUG = True
    SECRET_KEY = "jogo-trigonometria-dev"
    JSON_SORT_KEYS = False

    SWAGGER_TEMPLATE = {
        "swagger": "2.0",
        "info": {
            "title": "API - Jogo de Trigonometria",
            "description": "Backend para jogo educativo de funções trigonométricas.",
            "version": "1.0.0",
        },
        "basePath": "/",
    }
