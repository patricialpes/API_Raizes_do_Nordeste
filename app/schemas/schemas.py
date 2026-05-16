from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    produtoId: int
    quantidade: int


class PedidoCreate(BaseModel):
    usuarioId: int
    unidadeId: int
    canalPedido: str
    itens: List[Item]