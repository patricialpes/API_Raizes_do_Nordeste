# API_Raizes_do_Nordeste

API desenvolvida em FastAPI para gerenciamento de pedidos, produtos e pagamentos de uma rede de lanchonetes que busca rapidez e excelência no atendimento aos seus clientes.
Utiliza autenticação JWT e banco de dados MySQL.

## Tecnologias usadas
- Linguagem: Python
- Framework: FastAPI
- ORM: SQLAlchemy
- Banco de dados: MySQL
- Segurança: JWT
- Teste de API: Postman

## Como executar

 Antes de começar, verifique se possui instalado:
*   Python 3.x
*   Servidor MySQL ativo

### Passo a Passo

### 1. Criar ambiente virtual

python -m venv venv

## 2. Ativar ambiente virtual

venv\Scripts\activate

## 3. Instalar dependências

pip install -r requirements.txt

## 4. Rodar API

uvicorn app.main:app --reload

## Swagger

http://127.0.0.1:8000/docs

## Login

POST /api/auth/login

## Principais endpoints
POST /api/pedidos
GET /api/pedidos
POST /api/pagamentos/{id}?aprovado=true
GET /api/admin/pedidos
