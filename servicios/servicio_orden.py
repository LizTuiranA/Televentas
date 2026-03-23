"""Servicio de aplicación para gestionar órdenes de compra."""


class ServicioOrden:
    """Orquesta operaciones sobre las órdenes del sistema."""

    def __init__(self):
        self.ordenes = []
        self._secuencia = 1

    def crear_orden(self, cliente):
        """Crea y registra una nueva orden para un cliente."""
        numero = f"ORD-{self._secuencia:04d}"
        self._secuencia += 1
        orden = cliente.crear_orden(numero)
        self.ordenes.append(orden)
        return orden

    def agregar_producto(self, orden, producto, cantidad):
        """Agrega producto y cantidad a una orden existente."""
        orden.agregar_producto(producto, cantidad)

    def confirmar_orden(self, orden):
        """Confirma una orden validando sus reglas internas."""
        orden.confirmar()

    def cancelar_orden(self, orden):
        """Cancela una orden si aplica por estado."""
        orden.cancelar()
