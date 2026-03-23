"""Modelo de cliente de TeleVentas."""

from modelos.orden_compra import OrdenCompra
from modelos.queja import Queja


class Cliente:
    """Representa al cliente que realiza compras y consultas."""

    def __init__(self, id, nombre, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.suscrito_catalogo = False

    def solicitar_envio_catalogo(self):
        """Marca la suscripción al envío periódico del catálogo."""
        self.suscrito_catalogo = True

    def crear_orden(self, numero):
        """Crea una nueva orden para el cliente."""
        return OrdenCompra(numero=numero, cliente=self)

    def presentar_queja(self, id_queja, descripcion, orden_asociada=None):
        """Genera un objeto de queja asociado al cliente."""
        return Queja(
            id=id_queja,
            descripcion=descripcion,
            cliente=self,
            orden_asociada=orden_asociada,
        )
