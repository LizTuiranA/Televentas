"""Modelo principal de orden de compra."""

from datetime import datetime

from modelos.detalle_orden import DetalleOrden
from modelos.estados import EstadoOrden


class OrdenCompra:
    """Representa una orden creada por un cliente."""

    def __init__(self, numero, cliente):
        self.numero = numero
        self.fecha = datetime.now()
        self.estado = EstadoOrden.CREADA
        self.cliente = cliente
        self.detalles = []
        self.metodo_pago = None
        self.pago_exitoso = False

    def agregar_producto(self, producto, cantidad):
        """Agrega una línea de producto a la orden."""
        if self.estado in (EstadoOrden.CANCELADA, EstadoOrden.CONFIRMADA):
            raise ValueError("No se pueden agregar productos a esta orden.")

        if not producto.hay_disponibilidad(cantidad):
            raise ValueError("No hay stock suficiente para este producto.")

        detalle = DetalleOrden(producto, cantidad, producto.precio)
        self.detalles.append(detalle)
        self.estado = EstadoOrden.PENDIENTE_PAGO

    def calcular_total(self):
        """Suma los subtotales de todos los detalles."""
        return sum(detalle.calcular_subtotal() for detalle in self.detalles)

    def asignar_metodo_pago(self, metodo_pago):
        """Asigna el método de pago a la orden."""
        self.metodo_pago = metodo_pago

    def confirmar(self):
        """Confirma la orden si cumple reglas de negocio."""
        if self.estado == EstadoOrden.CANCELADA:
            raise ValueError("No se puede confirmar una orden cancelada.")

        if not self.detalles:
            raise ValueError("La orden no tiene productos.")

        if not self.metodo_pago or not self.pago_exitoso:
            raise ValueError("La orden requiere un pago aprobado.")

        self.estado = EstadoOrden.CONFIRMADA

    def cancelar(self):
        """Cancela la orden si aún no está confirmada."""
        if self.estado == EstadoOrden.CONFIRMADA:
            raise ValueError("No se puede cancelar una orden confirmada.")
        if self.estado == EstadoOrden.CANCELADA:
            raise ValueError("La orden ya está cancelada.")

        self.estado = EstadoOrden.CANCELADA
