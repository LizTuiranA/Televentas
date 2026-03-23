"""Enums de estados usados en el dominio de TeleVentas."""

from enum import Enum


class EstadoOrden(Enum):
    """Representa los posibles estados de una orden de compra."""

    CREADA = "CREADA"
    PENDIENTE_PAGO = "PENDIENTE_PAGO"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"


class EstadoPedido(Enum):
    """Representa los posibles estados del ciclo logístico de un pedido."""

    PENDIENTE = "PENDIENTE"
    ARMADO = "ARMADO"
    EMPAQUETADO = "EMPAQUETADO"
    DESPACHADO = "DESPACHADO"
    ENTREGADO = "ENTREGADO"


class EstadoQueja(Enum):
    """Representa los estados de atención de una queja."""

    REGISTRADA = "REGISTRADA"
    ENVIADA = "ENVIADA"
    EN_PROCESO = "EN_PROCESO"
    CERRADA = "CERRADA"
