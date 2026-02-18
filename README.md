![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-framework-009688)
![License](https://img.shields.io/github/license/FellypelimadaSilva/fastapi-pedidos-api)
![Repo Size](https://img.shields.io/github/repo-size/FellypelimadaSilva/fastapi-pedidos-api)
![Last Commit](https://img.shields.io/github/last-commit/FellypelimadaSilva/fastapi-pedidos-api)


#  FastAPI - Sistema de Pedidos

API REST desenvolvida com **FastAPI**, utilizando **JWT Authentication**, **SQLAlchemy**, **SQLite** e **Alembic** para controle de usuários e gerenciamento de pedidos.

---

##  Sobre o Projeto

Este projeto implementa um sistema completo de autenticação e gerenciamento de pedidos, incluindo:

- Cadastro de usuários
- Login com JWT
- Refresh Token
- Controle de permissões (admin e usuário comum)
- CRUD de pedidos
- Adição e remoção de itens
- Finalização e cancelamento de pedidos

Projeto desenvolvido com foco em boas práticas de backend, organização em camadas e segurança.

---

##  Arquitetura do Projeto

```
fastapi-pedidos-api/
│
├── app/
│   ├── main.py
│   ├── auth_routes.py
│   ├── order_routes.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│
├── alembic/
├── .env.example
├── requirements.txt
└── README.md
```

---

##  Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- JWT (python-jose)
- Passlib (bcrypt)

---

##  Autenticação

O sistema utiliza autenticação via **JWT Bearer Token**.

Após login, o usuário recebe:

- `access_token`
- `refresh_token`

Para acessar rotas protegidas, utilize:

```
Authorization: Bearer SEU_TOKEN_AQUI
```

---

##  Endpoints

###  Auth

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/auth/` | Rota base de autenticação |
| POST | `/auth/criar_conta` | Criar novo usuário |
| POST | `/auth/login` | Login via JSON |
| POST | `/auth/login-form` | Login via formulário OAuth2 |
| GET | `/auth/refresh` | Gerar novo access token |

---

###  Pedidos

| Método | Rota | Permissão |
|--------|------|-----------|
| GET | `/pedidos/` | Usuário autenticado |
| POST | `/pedidos/pedido` | Usuário autenticado |
| POST | `/pedidos/pedido/cancelar/{id}` | Admin |
| GET | `/pedidos/listar` | Admin |
| POST | `/pedidos/pedido/adicionar-item/{id}` | Dono ou Admin |
| POST | `/pedidos/pedido/remover-item/{id}` | Dono ou Admin |
| POST | `/pedidos/pedido/finalizar/{id}` | Admin |
| GET | `/pedidos/pedido/{id}` | Dono ou Admin |
| GET | `/pedidos/listar/pedidos-usuario` | Usuário autenticado |

---

##  Como Rodar o Projeto

### 1️ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/fastapi-pedidos-api.git
cd fastapi-pedidos-api
```

### 2️ Criar ambiente virtual

```bash
python -m venv venv
```

Ativar no Windows:
```bash
venv\Scripts\activate
```

Ativar no Linux/Mac:
```bash
source venv/bin/activate
```

### 3️ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️ Criar arquivo .env

Copie o arquivo `.env.example`:

```
SECRET_KEY=sua_chave_super_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./banco.db
```

### 5️ Rodar as migrations

```bash
alembic upgrade head
```

### 6️ Iniciar o servidor

```bash
uvicorn app.main:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

---

##  Documentação Interativa

O projeto possui documentação automática via Swagger:

```
/docs
```

---



## 👨‍💻 Autor

Desenvolvido por Fellype Lima da Silva

Projeto para fins de estudo e portfólio.
