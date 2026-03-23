"""Implementación de pago con tarjeta de crédito."""

from interfaces.metodo_pago import MetodoPago


class PagoTarjetaCredito(MetodoPago):
    """Simula la validación básica y el cobro de una tarjeta."""

    def __init__(self, titular, numero_tarjeta, cvv, fecha_vencimiento):
        self.titular = titular
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv
        self.fecha_vencimiento = fecha_vencimiento

    def procesar_pago(self, monto):
        """Valida datos mínimos y simula un pago aprobado."""
        numero_limpio = self.numero_tarjeta.replace(" ", "")
        datos_validos = (
            len(self.titular.strip()) >= 3
            and numero_limpio.isdigit()
            and 13 <= len(numero_limpio) <= 19
            and self.cvv.isdigit()
            and len(self.cvv) in (3, 4)
            and len(self.fecha_vencimiento.strip()) >= 4
        )

        if not datos_validos:
            return False

        # Simulación simple de aprobación.
        return monto > 0
