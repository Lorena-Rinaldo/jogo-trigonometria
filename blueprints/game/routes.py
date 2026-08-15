"""Define os endpoints da API relacionados ao jogo de trigonometria."""

from flask import jsonify, request

from blueprints.game import game_bp
from blueprints.game.schemas.game_schema import (
    validate_answer_payload,
    validate_final_code_payload,
    validate_hint_payload,
    validate_restart_payload,
)
from blueprints.game.schemas.player_schema import validate_player_payload
from blueprints.game.services.game_service import (
    answer_question,
    get_certificate,
    get_certificate_by_id,
    get_game_overview,
    get_player_progress,
    get_stage,
    get_stages,
    restart_player,
    restart_player_by_id,
    use_hint,
    validate_final_code,
)
from blueprints.game.services.player_service import create_player, get_characters


@game_bp.get("")
def game_overview():
    """
    Retorna um resumo geral do jogo.
    ---
    tags:
      - Jogo
    responses:
      200:
        description: Resumo com nome, objetivo, regras e classificações.
    """
    return jsonify(get_game_overview())


@game_bp.get("/stages")
def list_stages():
    """
    Lista todas as fases sem expor respostas corretas.
    ---
    tags:
      - Fases
    responses:
      200:
        description: Lista de fases do jogo.
    """
    return jsonify({"stages": get_stages()})


@game_bp.get("/characters")
def list_characters():
    """
    Lista os 5 personagens disponíveis para escolha.
    ---
    tags:
      - Jogador
    responses:
      200:
        description: Lista de personagens pré-prontos.
    """
    return jsonify({"characters": get_characters()})


@game_bp.post("/players")
def register_player():
    """
    Registra o nome do jogador e o personagem escolhido.
    ---
    tags:
      - Jogador
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - player_name
            - character_id
          properties:
            player_name:
              type: string
              example: Rubens
            character_id:
              type: integer
              example: 1
    responses:
      201:
        description: Jogador registrado com sucesso.
      400:
        description: Dados inválidos.
      404:
        description: Personagem não encontrado.
    """
    payload = request.get_json(silent=True) or {}
    errors = validate_player_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    result, status_code = create_player(payload["player_name"], payload["character_id"])
    return jsonify(result), status_code


@game_bp.get("/stages/<int:stage_id>")
def show_stage(stage_id):
    """
    Retorna uma fase com suas perguntas sem expor respostas corretas.
    ---
    tags:
      - Fases
    parameters:
      - name: stage_id
        in: path
        type: integer
        required: true
        description: ID da fase desejada.
    responses:
      200:
        description: Dados da fase solicitada.
      404:
        description: Fase não encontrada.
    """
    stage = get_stage(stage_id)
    if not stage:
        return jsonify({"error": "Fase não encontrada."}), 404

    return jsonify(stage)


@game_bp.post("/hint")
def request_hint():
    """
    Solicita uma dica para uma pergunta.
    ---
    tags:
      - Jogador
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - player_name
            - question_id
          properties:
            player_name:
              type: string
              example: Rubens
            question_id:
              type: integer
              example: 1
    responses:
      200:
        description: Dica liberada e progresso atualizado.
      400:
        description: Dados inválidos.
      404:
        description: Pergunta não encontrada.
    """
    payload = request.get_json(silent=True) or {}
    errors = validate_hint_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    result, status_code = use_hint(payload["player_name"], payload["question_id"])
    return jsonify(result), status_code


@game_bp.post("/answer")
def answer():
    """
    Envia uma resposta para uma pergunta.
    ---
    tags:
      - Jogador
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - player_name
            - question_id
            - selected_option
          properties:
            player_name:
              type: string
              example: Rubens
            question_id:
              type: integer
              example: 1
            selected_option:
              type: string
              example: b
    responses:
      200:
        description: Resultado da resposta e progresso do jogador.
      400:
        description: Dados inválidos.
      404:
        description: Pergunta não encontrada.
    """
    payload = request.get_json(silent=True) or {}
    errors = validate_answer_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    result, status_code = answer_question(
        payload["player_name"],
        payload["question_id"],
        payload["selected_option"],
    )
    return jsonify(result), status_code


@game_bp.get("/progress/<player_name>")
def progress(player_name):
    """
    Consulta o progresso de um jogador.
    ---
    tags:
      - Jogador
    parameters:
      - name: player_name
        in: path
        type: string
        required: true
        description: Nome do jogador.
    responses:
      200:
        description: Progresso atual do jogador.
    """
    return jsonify(get_player_progress(player_name))


@game_bp.post("/restart")
def restart():
    """
    Reinicia o progresso de um jogador.
    ---
    tags:
      - Jogador
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - player_name
          properties:
            player_name:
              type: string
              example: Rubens
    responses:
      200:
        description: Progresso reiniciado.
      400:
        description: Dados inválidos.
    """
    payload = request.get_json(silent=True) or {}
    errors = validate_restart_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    return jsonify(restart_player(payload["player_name"]))


@game_bp.post("/players/<player_id>/restart")
def restart_by_id(player_id):
    """
    Reinicia o progresso de um jogador pelo ID.
    ---
    tags:
      - Jogador
    parameters:
      - name: player_id
        in: path
        type: string
        required: true
        description: ID do jogador retornado no cadastro.
    responses:
      200:
        description: Progresso reiniciado.
      404:
        description: Jogador não encontrado.
    """
    result, status_code = restart_player_by_id(player_id)
    return jsonify(result), status_code


@game_bp.post("/final-code")
def final_code():
    """
    Valida o código final digitado pelo jogador.
    ---
    tags:
      - Código Final
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - player_name
            - code
          properties:
            player_name:
              type: string
              example: Rubens
            code:
              type: string
              example: VOCÊ DOMINOU AS FUNÇÕES TRIGONOMÉTRICAS
    responses:
      200:
        description: Resultado da validação do código final.
      400:
        description: Dados inválidos.
      403:
        description: Jogador ainda não pode validar o código final.
    """
    payload = request.get_json(silent=True) or {}
    errors = validate_final_code_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    result, status_code = validate_final_code(payload["player_name"], payload["code"])
    return jsonify(result), status_code


@game_bp.get("/certificate/<player_name>")
def certificate(player_name):
    """
    Retorna o certificado quando o jogador conclui o jogo.
    ---
    tags:
      - Certificado
    parameters:
      - name: player_name
        in: path
        type: string
        required: true
        description: Nome do jogador.
    responses:
      200:
        description: Certificado liberado.
      403:
        description: Jogo ainda não concluído.
    """
    result, status_code = get_certificate(player_name)
    return jsonify(result), status_code


@game_bp.get("/players/<player_id>/certificate")
def certificate_by_id(player_id):
    """
    Retorna o certificado pelo ID do jogador.
    ---
    tags:
      - Certificado
    parameters:
      - name: player_id
        in: path
        type: string
        required: true
        description: ID do jogador retornado no cadastro.
    responses:
      200:
        description: Certificado liberado.
      403:
        description: Jogo ainda não concluído.
      404:
        description: Jogador não encontrado.
    """
    result, status_code = get_certificate_by_id(player_id)
    return jsonify(result), status_code
