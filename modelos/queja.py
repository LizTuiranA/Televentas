"""Modelo de registro de quejas."""

from datetime import datetime

from modelos.estados import EstadoQueja


class Queja:
    """Representa una queja presentada por un cliente."""

    def __init__(self, id, descripcion, cliente, orden_asociada=None):
        self.id = id
        self.fecha = datetime.now()
        self.descripcion = descripcion
        self.estado = EstadoQueja.REGISTRADA
        self.cliente = cliente
        self.orden_asociada = orden_asociada

    def registrar(self):
        """Confirma el estado inicial de registro."""
        self.estado = EstadoQueja.REGISTRADA

    def cambiar_estado(self, nuevo_estado):
        """Actualiza el estado de la queja."""
        self.estado = nuevo_estado
