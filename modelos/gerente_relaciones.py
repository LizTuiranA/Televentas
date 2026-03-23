"""Modelo del gerente de relaciones con clientes."""

from modelos.estados import EstadoQueja


class GerenteRelaciones:
    """Responsable de recibir y dar curso a quejas."""

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def recibir_queja(self, queja):
        """Marca la queja como en proceso al recibirla."""
        queja.cambiar_estado(EstadoQueja.EN_PROCESO)
        return (
            f"El gerente {self.nombre} recibió la queja {queja.id} "
            f"del cliente {queja.cliente.nombre}."
        )
