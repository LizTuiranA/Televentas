"""Modelo de agente de depósito."""

from modelos.estados import EstadoOrden


class AgenteDeposito:
    """Representa al colaborador que prepara pedidos."""

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def consultar_ordenes_confirmadas(self, ordenes):
        """Filtra y retorna las órdenes confirmadas."""
        return [orden for orden in ordenes if orden.estado == EstadoOrden.CONFIRMADA]

    def preparar_pedido(self, pedido, servicio_inventario):
        """Arma el pedido y descuenta stock por cada detalle."""
        pedido.armar_pedido()
        for detalle in pedido.orden_compra.detalles:
            servicio_inventario.actualizar_stock(
                detalle.producto.codigo, detalle.cantidad
            )
