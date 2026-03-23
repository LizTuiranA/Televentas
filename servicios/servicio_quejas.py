"""Servicio de aplicación para registrar y escalar quejas."""

from modelos.estados import EstadoQueja


class ServicioQuejas:
    """Administra el ciclo básico de las quejas de clientes."""

    def __init__(self, gerente_relaciones):
        self.gerente_relaciones = gerente_relaciones
        self.quejas = []
        self._secuencia = 1

    def registrar_queja(self, cliente, descripcion, orden=None):
        """Registra una nueva queja en estado inicial."""
        id_queja = f"Q-{self._secuencia:04d}"
        self._secuencia += 1

        queja = cliente.presentar_queja(id_queja, descripcion, orden)
        queja.registrar()
        self.quejas.append(queja)
        return queja

    def notificar_queja(self, queja):
        """Remite la queja al gerente de relaciones."""
        queja.cambiar_estado(EstadoQueja.ENVIADA)
        return self.gerente_relaciones.recibir_queja(queja)
