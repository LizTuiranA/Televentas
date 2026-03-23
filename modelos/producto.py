"""Modelo de producto del catálogo."""


class Producto:
    """Representa un producto disponible para compra."""

    def __init__(self, codigo, descripcion, precio, cantidad_disponible):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = float(precio)
        self.cantidad_disponible = int(cantidad_disponible)

    def obtener_informacion(self):
        """Retorna una descripción legible del producto."""
        return (
            f"Código: {self.codigo} | Descripción: {self.descripcion} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.cantidad_disponible}"
        )

    def hay_disponibilidad(self, cantidad_solicitada):
        """Indica si hay unidades suficientes en stock."""
        return (
            cantidad_solicitada > 0 and self.cantidad_disponible >= cantidad_solicitada
        )
