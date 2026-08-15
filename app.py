"""Inicializa a aplicação Flask e registra os blueprints do projeto."""

from flask import Flask, jsonify

from blueprints.game import game_bp
from config import Config

try:
    from flasgger import Swagger
except ImportError:
    Swagger = None


def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(game_bp)

    if Swagger:
        Swagger(app, template=Config.SWAGGER_TEMPLATE)

    @app.get("/")
    def health_check():
        """
        Verifica se a API está online.
        ---
        tags:
          - Sistema
        responses:
          200:
            description: API funcionando corretamente.
        """
        return jsonify(
            {
                "status": "online",
                "message": "API do Jogo de Trigonometria funcionando.",
                "docs": "/apidocs/",
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
