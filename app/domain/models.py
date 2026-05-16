from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, DateTime
from app.infrastructure.database import Base
from datetime import datetime
import enum


class CanalPedido(str, enum.Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(255))
    perfil = Column(Enum("CLIENTE", "ADMIN", "GERENTE"))


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    preco = Column(Float)
    estoque = Column(Integer)


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    unidade_id = Column(Integer, ForeignKey("unidade.id"))
    canal = Column(Enum(CanalPedido))
    status = Column(String(50))
    total = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    
class Unidade(Base):
    __tablename__ = "unidade"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    endereco = Column(String(255))