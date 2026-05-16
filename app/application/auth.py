from jose import jwt
from datetime import datetime, timedelta

SECRET = "segredo"
ALGORITHM = "HS256"


def gerar_token(data: dict):
    dados = data.copy()
    dados["exp"] = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode(dados, SECRET, algorithm=ALGORITHM)


def hash_senha(senha: str):
    return senha  # não criptografa


def verificar_senha(senha: str, senha_banco: str):
    return senha == senha_banco