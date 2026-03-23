"""Interfaz para envío de correos."""

from abc import ABC, abstractmethod


class ServicioCorreo(ABC):
    """Contrato para servicios de notificación por correo."""

    @abstractmethod
    def enviar_catalogo(self, cliente, catalogo):
        """Envía el catálogo al correo del cliente."""
