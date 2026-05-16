from sqlalchemy.orm import Session
from app.domain.models import Pedido, Produto, ItemPedido


def criar_pedido(db: Session, data):
    total = 0
    itens_db = []

    for item in data.itens:
        produto = db.query(Produto).filter(Produto.id == item.produtoId).first()

        if not produto:
            raise Exception("PRODUTO_NAO_ENCONTRADO")

        if produto.estoque < item.quantidade:
            raise Exception("ESTOQUE_INSUFICIENTE")

        total += produto.preco * item.quantidade
        produto.estoque -= item.quantidade

        itens_db.append(
            ItemPedido(
                produto_id=produto.id,
                quantidade=item.quantidade,
                preco_unitario=produto.preco
            )
        )

    pedido = Pedido(
        usuario_id=data.usuarioId,
        unidade_id=data.unidadeId,
        canal=data.canalPedido,
        status="PENDENTE",
        total=total
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    for item in itens_db:
        item.pedido_id = pedido.id
        db.add(item)

    db.commit()

    return pedido


def pagamento_mock(db: Session, pedido_id: int, aprovado: bool):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise Exception("PEDIDO_NAO_ENCONTRADO")

    pedido.status = "FINALIZADO" if aprovado else "CANCELADO"

    db.commit()

    return pedido