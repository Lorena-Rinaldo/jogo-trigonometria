# 📐 Jogo de Trigonometria 📐

*Um backend em Flask para um jogo educativo de aprendizado e desafios matemáticos.*

Bem-vindo ao projeto **Jogo de Trigonometria**! Esta aplicação foi desenvolvida para proporcionar uma experiência de aprendizado interativa sobre funções trigonométricas, com fases, personagens, dicas, progresso do jogador e validação de respostas. O projeto combina lógica de jogo, persistência de dados e documentação de API para facilitar testes e integração.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Como Executar o Projeto Localmente](#como-executar-o-projeto-localmente)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Banco de Dados](#banco-de-dados)
- [Principais Rotas da API](#principais-rotas-da-api)
- [Contato](#contato)

## Sobre o Projeto

O objetivo principal deste projeto é transformar o estudo de trigonometria em uma experiência dinâmica e envolvente. O jogo oferece fases progressivas, perguntas contextualizadas e desafios que exigem raciocínio matemático. A API gerencia o cadastro de jogadores, a escolha de personagens, a leitura das fases, a validação de respostas e o acompanhamento de desempenho durante toda a partida.

A aplicação também permite que o jogador receba dicas, avance entre etapas, reinicie o progresso e obtenha um certificado ao concluir o jogo. Tudo isso é acompanhado por uma documentação Swagger, o que facilita a utilização e os testes das rotas da API.

## Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

- **Python**: linguagem principal do backend.
- **Flask**: framework utilizado para criar a API REST.
- **Flasgger**: documentação automática da API em Swagger.
- **Supabase**: plataforma utilizada para persistência dos dados dos jogadores e do progresso.
- **PostgreSQL**: banco de dados relacional gerenciado pelo Supabase.
- **Pydantic**: validação de payloads de entrada.
- **Dotenv**: carregamento de variáveis de ambiente.
- **JSON**: estrutura de comunicação entre cliente e servidor.

## Funcionalidades Implementadas

- **Cadastro de Jogador**:
  - Registro do nome do jogador.
  - Seleção de personagem disponível.
- **Escolha de Personagens**:
  - Listagem de personagens pré-definidos para integração com a experiência do jogo.
- **Listagem de Fases**:
  - Visualização das etapas do jogo sem expor as respostas corretas.
- **Acesso a Fase Específica**:
  - Recuperação detalhada de uma fase e suas perguntas.
- **Dicas por Pergunta**:
  - Solicitação de ajuda para o jogador durante a partida.
- **Validação de Respostas**:
  - Verificação da resposta escolhida pelo usuário.
  - Atualização de pontuação, erros e progresso.
- **Progresso do Jogador**:
  - Consulta do status atual, fases concluídas e desempenho geral.
- **Reinício de Partida**:
  - Reinício do progresso do jogador por nome ou por ID.
- **Código Final**:
  - Validação de código final para conclusão do jogo.
- **Certificado de Conclusão**:
  - Geração de retorno do certificado após a conclusão das exigências do jogo.
- **Documentação da API**:
  - Endpoints acessíveis via Swagger em /apidocs.

## Como Executar o Projeto Localmente

Siga os passos abaixo para rodar este projeto na sua máquina.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/jogo-trigonometria.git
cd jogo-trigonometria
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_URL=sua-url-do-supabase
SUPABASE_SECRET_KEY=sua-chave-secreta-do-backend
```

> Importante: o arquivo `.env` não deve ser enviado para o GitHub.

### 5. Crie as tabelas no banco

Execute o SQL contido no arquivo:

```text
database/schema.sql
```

### 6. Inicie a aplicação

```bash
python app.py
```

A aplicação será iniciada em:

```text
http://localhost:5000
```

A documentação Swagger ficará disponível em:

```text
http://localhost:5000/apidocs/
```

## Estrutura do Projeto

A estrutura atual do repositório está organizada da seguinte forma:

```text
.
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── blueprints/
│   └── game/
│       ├── __init__.py
│       ├── routes.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── characters.py
│       │   ├── exercises.py
│       │   ├── stages.py
│       │   └── story.py
│       ├── schemas/
│       │   ├── __init__.py
│       │   ├── game_schema.py
│       │   └── player_schema.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── game_service.py
│       │   ├── player_service.py
│       │   ├── progress_service.py
│       │   └── score_service.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── database/
│   ├── __init__.py
│   ├── schema.sql
│   └── supabase_client.py
└── .env
```

### Observações

- A pasta `blueprints/game` concentra a lógica principal da API.
- Os dados de personagens, fases e perguntas ficam em `blueprints/game/data`.
- A aplicação usa `database/schema.sql` para criação das tabelas essenciais.
- O arquivo `.env` é necessário para configurar a conexão com o Supabase.

## Banco de Dados

O backend utiliza o Supabase para armazenar informações dos jogadores e seu progresso no jogo. Os principais dados persistidos incluem:

- nome do jogador
- personagem escolhido
- estágio atual
- pontuação
- quantidade de respostas erradas
- perguntas respondidas
- fases concluídas
- códigos desbloqueados
- uso de dicas
- status de conclusão e fim de jogo

A estrutura inicial do banco é criada pelo arquivo:

```text
database/schema.sql
```

## Principais Rotas da API

A API possui os seguintes endpoints principais:

```text
GET /
GET /game
GET /game/characters
POST /game/players
GET /game/stages
GET /game/stages/<stage_id>
POST /game/hint
POST /game/answer
GET /game/progress/<player_name>
POST /game/restart
POST /game/players/<player_id>/restart
POST /game/final-code
GET /game/certificate/<player_name>
GET /game/players/<player_id>/certificate
```

Também é possível consultar e testar todos os endpoints diretamente pela interface do Swagger em:

```text
http://localhost:5000/apidocs/
```

## Contato

Projeto desenvolvido com foco em aprendizado, educação e interatividade.

- **GitHub**: https://github.com/Lorena-Rinaldo
- **LinkedIn**: https://www.linkedin.com/in/lorena-rinaldo01
- **Email**: lorena.rinaldodev@gmail.com

🧠 Aprender trigonometria pode ser desafiador, mas com prática e interação, cada etapa se torna mais clara. ✅
