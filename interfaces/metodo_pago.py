"""Interfaz para métodos de pago."""

from abc import ABC, abstractmethod


class MetodoPago(ABC):
    """Contrato para procesar pagos."""

    @abstractmethod
    def procesar_pago(self, monto):
        """Procesa el pago y retorna True/False según resultado."""
