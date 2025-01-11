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
1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

##### Cacheando os dados
1. Cache Embrapa data:

```bash
python3 -m app.scripts.cache_embrapa
```

2. Start the API server:

```bash
uvicorn app.main:app --reload
```

The server will start at http://localhost:8000

### API Endpoints

#### Authentication

- POST /api/v1/auth/login - Login with username and password
- POST /api/v1/auth/sign-in - Create new account
- PUT /api/v1/auth/update_password - Update password (requires authentication)

#### Embrapa Data

- GET /api/v1/embrapa/query - Get viticulture data (requires authentication)
- GET /api/v1/embrapa/description - Get data descriptions (requires authentication)

#### Documentation

API documentation is available at:

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/api/v1/openapi.json

#### Database
The application uses SQLite with the following main table:

- dados_vitivinicultura: Stores all viticulture data from Embrapa

#### Environment Variables
Create a .env file with:

```TEXT
PROJECT_NAME=TECH_CHALLENGE_1
VERSION=0.0.1-SNAPSHOT
API_V1_STR=/api/v1
```

#### Security
- JWT token-based authentication
- Protected routes using JWT verification
- Token expiration: 5 minutes
#### Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

#### License
MIT License