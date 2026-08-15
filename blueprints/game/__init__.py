"""Cria e expõe o blueprint responsável pelas rotas do jogo."""

from flask import Blueprint

game_bp = Blueprint("game", __name__, url_prefix="/game")

from blueprints.game import routes  # noqa: E402,F401
