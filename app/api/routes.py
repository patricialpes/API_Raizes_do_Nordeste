from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.infrastructure.database import SessionLocal
from app.domain.models import User, Pedido
from app.schemas.schemas import PedidoCreate
from app.application.services import criar_pedido, pagamento_mock

# CONFIGURAÇÃO JWT
SECRET = "segredo"
ALGORITHM = "HS256"

router = APIRouter()

# CONEXÃO COM BANCO
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GERAR TOKEN
def gerar_token(user):
    payload = {
        "sub": user.email,
        "perfil": user.perfil
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


# VALIDAR TOKEN (401)
def verificar_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token ausente")

    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


#  VALIDAR ADMIN (403)
def verificar_admin(payload = Depends(verificar_token)):
    if payload.get("perfil") != "ADMIN":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return payload


# LOGIN
@router.post("/auth/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data["email"]).first()

    if not user or user.senha != data["senha"]:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = gerar_token(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# CRIAR PEDIDO (PRECISA LOGIN)
@router.post("/pedidos")
def criar(
    data: PedidoCreate,
    db: Session = Depends(get_db),
    user = Depends(verificar_token)
):
    try:
        pedido = criar_pedido(db, data)
        return {
            "pedidoId": pedido.id,
            "status": pedido.status,
            "total": pedido.total
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PAGAMENTO (PRECISA LOGIN)
@router.post("/pagamentos/{pedido_id}")
def pagar(
    pedido_id: int,
    aprovado: bool,
    db: Session = Depends(get_db),
    user = Depends(verificar_token)
):
    try:
        pedido = pagamento_mock(db, pedido_id, aprovado)
        return {"status": pedido.status}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# LISTAR PEDIDOS (PRECISA LOGIN)
@router.get("/pedidos")
def listar(
    canalPedido: str = None,
    db: Session = Depends(get_db),
    user = Depends(verificar_token)
):
    query = db.query(Pedido)

    if canalPedido:
        query = query.filter(Pedido.canal == canalPedido)

    return query.all()


# ROTA ADMIN (403)
@router.get("/admin/pedidos")
def pedidos_admin(
    db: Session = Depends(get_db),
    user = Depends(verificar_admin)
):
    return db.query(Pedido).all()