"""Implementación simulada de servicio de inventario."""

from interfaces.servicio_inventario import ServicioInventario


class InventarioExternoService(ServicioInventario):
    """Simula una integración externa para consultar y actualizar stock."""

    def __init__(self, catalogo):
        self.catalogo = catalogo

    def consultar_producto(self, codigo):
        """Consulta un producto en el catálogo local en memoria."""
        return self.catalogo.buscar_producto_por_codigo(codigo)

    def actualizar_stock(self, codigo, cantidad):
        """Descuenta stock simulando la respuesta de un servicio externo."""
        producto = self.consultar_producto(codigo)
        if producto is None:
            raise ValueError("Producto no encontrado en inventario.")

        if cantidad <= 0:
            raise ValueError("La cantidad para actualizar stock debe ser positiva.")

        if producto.cantidad_disponible < cantidad:
            raise ValueError(
                f"Stock insuficiente para {producto.codigo}. "
                f"Disponible: {producto.cantidad_disponible}."
            )

        producto.cantidad_disponible -= cantidad
        return producto.cantidad_disponible
