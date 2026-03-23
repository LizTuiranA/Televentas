"""Punto de entrada del sistema de consola TeleVentas."""

from implementaciones.correo_electronico_service import CorreoElectronicoService
from implementaciones.inventario_externo_service import InventarioExternoService
from implementaciones.pago_tarjeta_credito import PagoTarjetaCredito
from modelos.agente_deposito import AgenteDeposito
from modelos.catalogo import Catalogo
from modelos.cliente import Cliente
from modelos.empresa_transporte import EmpresaTransporte
from modelos.estados import EstadoOrden
from modelos.gerente_relaciones import GerenteRelaciones
from modelos.pedido import Pedido
from modelos.producto import Producto
from servicios.servicio_logistica import ServicioLogistica
from servicios.servicio_orden import ServicioOrden
from servicios.servicio_quejas import ServicioQuejas


def cargar_datos_iniciales():
    """Construye datos de prueba en memoria para el sistema."""
    productos = [
        Producto("P001", "Auriculares Bluetooth", 149.90, 20),
        Producto("P002", "Teclado mecánico", 320.00, 15),
        Producto("P003", "Mouse inalámbrico", 95.50, 30),
        Producto("P004", "Monitor 24 pulgadas", 890.00, 8),
        Producto("P005", "Webcam HD", 180.00, 12),
    ]
    catalogo = Catalogo(productos)

    transportadoras = [
        EmpresaTransporte("Express Sur", 18.00, True),
        EmpresaTransporte("Carga Rápida", 22.50, True),
        EmpresaTransporte("LogiNorte", 25.00, False),
    ]

    cliente = Cliente(
        id="C-001", nombre="Ana Torres", correo_electronico="ana@correo.com"
    )
    gerente = GerenteRelaciones("Carlos Mejía", "gerencia@televentas.com")
    agente = AgenteDeposito(id="A-01", nombre="Luis Pérez")

    return catalogo, transportadoras, cliente, gerente, agente


def mostrar_menu_principal():
    """Imprime el menú principal de opciones."""
    print("\n=== SISTEMA TELEVENTAS ===")
    print("1. Ver catálogo de productos")
    print("2. Consultar producto por código")
    print("3. Solicitar envío del catálogo por correo")
    print("4. Crear nueva orden de compra")
    print("5. Ver orden actual")
    print("6. Agregar producto a la orden actual")
    print("7. Procesar pago de la orden")
    print("8. Confirmar orden")
    print("9. Cancelar orden")
    print("10. Preparar pedido")
    print("11. Empaquetar pedido")
    print("12. Seleccionar empresa transportadora")
    print("13. Despachar pedido")
    print("14. Registrar queja")
    print("15. Ver estado del pedido")
    print("16. Comprobar quejas")
    print("17. Salir")


def mostrar_quejas(quejas):
    """Muestra en consola las quejas registradas."""
    if not quejas:
        print("No hay quejas registradas.")
        return

    print("\n--- QUEJAS REGISTRADAS ---")
    for queja in quejas:
        orden = queja.orden_asociada.numero if queja.orden_asociada else "Sin orden"
        print(
            f"{queja.id} | Estado: {queja.estado.value} | "
            f"Cliente: {queja.cliente.nombre} | Orden: {orden}"
        )
        print(f"Descripción: {queja.descripcion}")


def mostrar_orden(orden):
    """Muestra en consola la información de la orden actual."""
    if orden is None:
        print("No hay una orden activa en memoria.")
        return

    print("\n--- ORDEN ACTUAL ---")
    print(f"Número: {orden.numero}")
    print(f"Fecha: {orden.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Cliente: {orden.cliente.nombre}")
    print(f"Estado: {orden.estado.value}")
    print(f"Pago exitoso: {'Sí' if orden.pago_exitoso else 'No'}")

    if not orden.detalles:
        print("Sin productos agregados.")
    else:
        for i, detalle in enumerate(orden.detalles, start=1):
            print(
                f"{i}. {detalle.producto.descripcion} | "
                f"Cantidad: {detalle.cantidad} | "
                f"P. Unitario: ${detalle.precio_unitario:.2f} | "
                f"Subtotal: ${detalle.calcular_subtotal():.2f}"
            )
        print(f"Total: ${orden.calcular_total():.2f}")


def leer_entero(mensaje):
    """Lee un número entero con manejo básico de error."""
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def ejecutar_aplicacion():
    """Controla el ciclo principal de interacción por consola."""
    catalogo, transportadoras, cliente, gerente, agente = cargar_datos_iniciales()

    servicio_orden = ServicioOrden()
    servicio_logistica = ServicioLogistica()
    servicio_quejas = ServicioQuejas(gerente)
    servicio_correo = CorreoElectronicoService()
    servicio_inventario = InventarioExternoService(catalogo)

    orden_actual = None
    pedido_actual = None
    secuencia_pedido = 1

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                print("\n--- CATÁLOGO DE PRODUCTOS ---")
                for producto in catalogo.listar_productos():
                    print(producto.obtener_informacion())

            elif opcion == "2":
                codigo = input("Ingrese código de producto: ").strip()
                producto = servicio_inventario.consultar_producto(codigo)
                if producto:
                    print(producto.obtener_informacion())
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                cliente.solicitar_envio_catalogo()
                mensaje = servicio_correo.enviar_catalogo(cliente, catalogo)
                print(mensaje)

            elif opcion == "4":
                orden_actual = servicio_orden.crear_orden(cliente)
                pedido_actual = None
                print(f"Orden {orden_actual.numero} creada correctamente.")

            elif opcion == "5":
                mostrar_orden(orden_actual)

            elif opcion == "6":
                if orden_actual is None:
                    print("Primero debe crear una orden.")
                    continue

                codigo = input("Código del producto: ").strip()
                producto = catalogo.buscar_producto_por_codigo(codigo)
                if producto is None:
                    print("Producto no encontrado en catálogo.")
                    continue

                cantidad = leer_entero("Cantidad a agregar: ")
                servicio_orden.agregar_producto(orden_actual, producto, cantidad)
                print("Producto agregado correctamente.")

            elif opcion == "7":
                if orden_actual is None:
                    print("No existe una orden para procesar pago.")
                    continue

                if not orden_actual.detalles:
                    print("La orden no tiene productos, no se puede pagar.")
                    continue

                print("\nIngrese datos de tarjeta de crédito")
                titular = input("Titular: ").strip()
                numero = input("Número de tarjeta: ").strip()
                cvv = input("CVV: ").strip()
                fecha_vencimiento = input("Fecha vencimiento (MM/AA): ").strip()

                metodo_pago = PagoTarjetaCredito(
                    titular=titular,
                    numero_tarjeta=numero,
                    cvv=cvv,
                    fecha_vencimiento=fecha_vencimiento,
                )

                orden_actual.asignar_metodo_pago(metodo_pago)
                monto = orden_actual.calcular_total()
                orden_actual.pago_exitoso = metodo_pago.procesar_pago(monto)

                if orden_actual.pago_exitoso:
                    print(f"Pago aprobado por ${monto:.2f}.")
                else:
                    print("Pago rechazado. Verifique los datos de la tarjeta.")

            elif opcion == "8":
                if orden_actual is None:
                    print("No existe una orden para confirmar.")
                    continue

                servicio_orden.confirmar_orden(orden_actual)
                print(f"Orden {orden_actual.numero} confirmada.")

            elif opcion == "9":
                if orden_actual is None:
                    print("No existe una orden para cancelar.")
                    continue

                servicio_orden.cancelar_orden(orden_actual)
                pedido_actual = None
                print(f"Orden {orden_actual.numero} cancelada.")

            elif opcion == "10":
                if orden_actual is None:
                    print("No existe orden actual.")
                    continue

                confirmadas = agente.consultar_ordenes_confirmadas(
                    servicio_orden.ordenes
                )
                if not confirmadas:
                    print("No hay órdenes confirmadas para preparar.")
                    continue

                if orden_actual.estado != EstadoOrden.CONFIRMADA:
                    print("La orden actual no está confirmada.")
                    continue

                if pedido_actual is None:
                    pedido_id = f"PED-{secuencia_pedido:04d}"
                    secuencia_pedido += 1
                    pedido_actual = Pedido(id=pedido_id, orden_compra=orden_actual)

                agente.preparar_pedido(pedido_actual, servicio_inventario)
                print(f"Pedido {pedido_actual.id} preparado por {agente.nombre}.")

            elif opcion == "11":
                if pedido_actual is None:
                    print("Primero debe preparar un pedido.")
                    continue

                pedido_actual.empaquetar()
                print(f"Pedido {pedido_actual.id} empaquetado correctamente.")

            elif opcion == "12":
                if pedido_actual is None:
                    print("No hay un pedido activo para asignar transporte.")
                    continue

                print("\nTransportadoras disponibles:")
                for i, empresa in enumerate(transportadoras, start=1):
                    estado = "Disponible" if empresa.disponible else "No disponible"
                    print(
                        f"{i}. {empresa.nombre} | Costo base: ${empresa.costo_base:.2f} | {estado}"
                    )

                seleccion = leer_entero("Seleccione número de transportadora: ") - 1
                empresa = servicio_logistica.seleccionar_transportadora(
                    pedido_actual,
                    transportadoras,
                    seleccion,
                )
                print(f"Transportadora asignada: {empresa.nombre}.")

            elif opcion == "13":
                if pedido_actual is None:
                    print("No hay pedido para despachar.")
                    continue

                mensaje = servicio_logistica.despachar_pedido(pedido_actual)
                print(f"Pedido {pedido_actual.id} despachado.")
                print(mensaje)

            elif opcion == "14":
                descripcion = input("Describa la queja: ").strip()
                if not descripcion:
                    print("La descripción no puede estar vacía.")
                    continue

                asociar = (
                    input("¿Desea asociar la queja a la orden actual? (s/n): ")
                    .strip()
                    .lower()
                )
                orden_asociada = orden_actual if asociar == "s" else None

                queja = servicio_quejas.registrar_queja(
                    cliente=cliente,
                    descripcion=descripcion,
                    orden=orden_asociada,
                )
                mensaje = servicio_quejas.notificar_queja(queja)
                print(f"Queja {queja.id} registrada y remitida.")
                print(mensaje)

            elif opcion == "15":
                if pedido_actual is None:
                    print("No existe un pedido creado para la orden actual.")
                else:
                    transporte = (
                        pedido_actual.empresa_transporte.nombre
                        if pedido_actual.empresa_transporte
                        else "Sin asignar"
                    )
                    print(f"Pedido: {pedido_actual.id}")
                    print(f"Estado: {pedido_actual.estado.value}")
                    print(f"Transportadora: {transporte}")

            elif opcion == "16":
                mostrar_quejas(servicio_quejas.quejas)

            elif opcion == "17":
                print("Gracias por usar TeleVentas. Hasta pronto.")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as error:
            print(f"No fue posible completar la acción: {error}")
        except Exception as error:  # pragma: no cover
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_aplicacion()
