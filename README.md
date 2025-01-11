## Embrapa API

Uma RESTful API que provê acesso aos dados de vitivinicultura da Embrapa

#### Features
- Autenticacao JWT
- SQLite database para cachear os dados
- Scraping do site da Embrapa
- Endpoints protegidos por JWT
- Gestão de contas de usuários

#### Technology Stack

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite
- JWT for authentication

#### Estrutura do projeto

```TEXT
app/
├── api/              # rotas e endpoints
├── core/             # Core configurations
├── models/           # SQLAlchemy models
├── schemas/          # Pydantic schemas
├── scripts/          # Data caching scripts
└── utils/            # Utility functions
```

#### Instalando e rodando com o Docker (recomendado)

na pasta raiz do projeto execute:

```bash
docker-compose up --build
```

O servidor vai iniciar em http://localhost:8000


#### Instalando e rodando sem o Docker
1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Cache Embrapa data:

```bash
python3 -m app.scripts.cache_embrapa
```

4. Inicia o Servidor:

```bash
uvicorn app.main:app --reload
```

O servidor vai iniciar em http://localhost:8000

### API Endpoints

#### Autenticação

- POST /api/v1/auth/login - login com usuário e senha
- POST /api/v1/auth/sign-in - Cria um novo usuário

#### Embrapa Data

- GET /api/v1/embrapa/query - Recupera dados de vitivinicultura (requer autenticação)
- GET /api/v1/embrapa/description - Recupera dados de descrição (requer autenticação)

#### Documentação

Documentação da API disponível em:

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/api/v1/openapi.json

#### Database
A aplicação utiliza sqlite

- dados_vitivinicultura: Guarda todos os dados de vitivinicultura da embrapa
- dados_usuarios: Guarda os dados das contas de usuários