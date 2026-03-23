"""Modelo de pedido para la etapa logística."""

from modelos.estados import EstadoPedido, EstadoOrden


class Pedido:
    """Representa la preparación y despacho de una orden confirmada."""

    def __init__(self, id, orden_compra):
        self.id = id
        self.orden_compra = orden_compra
        self.estado = EstadoPedido.PENDIENTE
        self.empresa_transporte = None

    def armar_pedido(self):
        """Cambia el estado a armado si la orden está confirmada."""
        if self.orden_compra.estado != EstadoOrden.CONFIRMADA:
            raise ValueError("Solo se puede armar un pedido de una orden confirmada.")
        if self.estado != EstadoPedido.PENDIENTE:
            raise ValueError("El pedido no está en estado pendiente.")

        self.estado = EstadoPedido.ARMADO

    def empaquetar(self):
        """Empaqueta el pedido después de armarlo."""
        if self.estado != EstadoPedido.ARMADO:
            raise ValueError("Solo se puede empaquetar un pedido armado.")

        self.estado = EstadoPedido.EMPAQUETADO

    def asignar_transporte(self, empresa_transporte):
        """Asigna la transportadora para el despacho."""
        if not empresa_transporte.disponible:
            raise ValueError(
                "La empresa de transporte seleccionada no está disponible."
            )

        self.empresa_transporte = empresa_transporte

    def despachar(self):
        """Despacha el pedido cuando está listo para envío."""
        if self.estado != EstadoPedido.EMPAQUETADO:
            raise ValueError("Solo se puede despachar un pedido empaquetado.")
        if self.empresa_transporte is None:
            raise ValueError(
                "Debe asignar una empresa transportadora antes de despachar."
            )

        self.estado = EstadoPedido.DESPACHADO
