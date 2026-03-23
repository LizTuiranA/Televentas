"""Interfaz para servicio de inventario."""

from abc import ABC, abstractmethod


class ServicioInventario(ABC):
    """Contrato del servicio de inventario externo o simulado."""

    @abstractmethod
    def consultar_producto(self, codigo):
        """Retorna información del producto por código."""

    @abstractmethod
    def actualizar_stock(self, codigo, cantidad):
        """Descuenta o actualiza stock del producto indicado."""
