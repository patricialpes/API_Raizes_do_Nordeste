# API_Raizes_do_Nordeste

API desenvolvida em **FastAPI** para gerenciamento de pedidos, produtos e pagamentos de uma rede de lanchonetes que busca rapidez e excelência no atendimento aos seus clientes.  
Utiliza autenticação **JWT** e banco de dados **MySQL**.

## Tecnologia utilizada
- Linguagem: Python
- Framework: FastAPI
- ORM: SQLAlchemy
- Banco de dados: MySQL
- Segurança: JWT
- Teste de API: Postman
  
## Como executar

verifique se possui instalado:
-   Python 3.x
-   Servidor MySQL ativo

### Passo a Passo

### 1. Criar ambiente virtual

python -m venv venv

## 2. Ativar ambiente virtual

venv\Scripts\activate

## 3. Instalar dependências

pip install -r requirements.txt

## 4. Rodar a API

uvicorn app.main:app --reload

## Documentação Swagger

http://127.0.0.1:8000/docs

## Autenticação

POST /api/auth/login

## Rotas
- POST /api/pedidos
- GET /api/pedidos
- POST /api/pagamentos/{id}?aprovado=true
- GET /api/admin/pedidos
