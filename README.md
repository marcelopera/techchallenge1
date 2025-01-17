## Embrapa API

Uma RESTful API que provê acesso aos dados de vitivinicultura da Embrapa

### Casos de Uso para Machine Learning

#### Análise Preditiva de Produção
- Utilizar os dados históricos de produção vitivinícola para prever safras futuras
- Criar modelos de regressão para estimar produção baseado em anos anteriores
- Identificar tendências sazonais na produção de diferentes tipos de uva

#### Otimização de Preços
- Análise da relação entre quantidade produzida e valores de mercado
- Previsão de preços baseada em séries temporais
- Identificação de fatores que influenciam na valorização dos produtos

#### Segmentação de Produtos
- Clustering dos tipos de produtos por características similares
- Análise de padrões de produção por região
- Identificação de nichos de mercado baseado nos dados históricos

#### Análise de Impacto Econômico
- Correlação entre produção vitivinícola e indicadores econômicos
- Previsão de impacto econômico baseado em variações de produção
- Identificação de padrões de crescimento do setor

#### Detecção de Anomalias
- Identificação de dados atípicos na produção
- Detecção de variações anormais nos preços
- Monitoramento de padrões incomuns no setor

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
1. Clone o repositório e entre nele

```bash
cd techchallenge1
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicia o Servidor:

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