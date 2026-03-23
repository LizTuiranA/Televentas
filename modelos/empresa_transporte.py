"""Modelo de empresa transportadora."""

from modelos.estados import EstadoPedido


class EmpresaTransporte:
    """Representa una empresa de logística de última milla."""

    def __init__(self, nombre, costo_base, disponible=True):
        self.nombre = nombre
        self.costo_base = float(costo_base)
        self.disponible = disponible

    def entregar_pedido(self, pedido):
        """Simula la entrega final del pedido al cliente."""
        pedido.estado = EstadoPedido.ENTREGADO
        return (
            f"La empresa {self.nombre} entregó el pedido {pedido.id} "
            f"al cliente {pedido.orden_compra.cliente.nombre}."
        )
