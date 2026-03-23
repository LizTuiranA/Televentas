"""Implementación simulada del servicio de correo."""

from interfaces.servicio_correo import ServicioCorreo


class CorreoElectronicoService(ServicioCorreo):
    """Simula el envío por correo del catálogo de productos."""

    def enviar_catalogo(self, cliente, catalogo):
        """Imprime un mensaje de envío exitoso en consola."""
        total = len(catalogo.listar_productos())
        return (
            f"Catálogo enviado a {cliente.correo_electronico} "
            f"con {total} productos disponibles."
        )
