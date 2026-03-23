"""Servicio de aplicación para la logística de pedidos."""


class ServicioLogistica:
    """Orquesta selección de transporte y despacho de pedidos."""

    def seleccionar_transportadora(self, pedido, transportadoras, indice):
        """Asigna una empresa transportadora por índice seleccionado."""
        if not transportadoras:
            raise ValueError("No hay transportadoras disponibles para seleccionar.")

        if indice < 0 or indice >= len(transportadoras):
            raise ValueError("Índice de transportadora inválido.")

        empresa = transportadoras[indice]
        pedido.asignar_transporte(empresa)
        return empresa

    def despachar_pedido(self, pedido):
        """Despacha el pedido y simula su entrega por transportadora."""
        pedido.despachar()
        mensaje = pedido.empresa_transporte.entregar_pedido(pedido)
        return mensaje
