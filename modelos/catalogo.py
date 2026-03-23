"""Modelo de catálogo de productos."""


class Catalogo:
    """Administra el conjunto de productos disponibles."""

    def __init__(self, productos=None):
        self.productos = productos if productos is not None else []

    def listar_productos(self):
        """Retorna todos los productos cargados en memoria."""
        return self.productos

    def buscar_producto_por_codigo(self, codigo):
        """Busca un producto por su código único."""
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None
