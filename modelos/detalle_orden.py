"""Detalle de línea para una orden de compra."""


class DetalleOrden:
    """Representa la relación entre producto y cantidad en una orden."""

    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    def calcular_subtotal(self):
        """Calcula el subtotal de este detalle."""
        return self.cantidad * self.precio_unitario
