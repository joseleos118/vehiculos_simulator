from clases.vehiculos import Vehiculo, Coche, Moto


flota = []


def mostrar_menu():
    """Muestra el menú principal."""

    print("\n")
    print("-" * 50)
    print("       SISTEMA DE GESTIÓN DE VEHÍCULOS")
    print("-" * 50)
    print("1. Registrar coche")
    print("2. Registrar moto")
    print("3. Mostrar flota")
    print("4. Encender/Apagar vehículo")
    print("5. Calcular alquiler")
    print("6. Alquilar vehículo")
    print("7. Devolver vehículo")
    print("8. Ver estadísticas")
    print("9. Dar de baja vehículo")
    print("10. Salir")
    print("-" * 50)


def mostrar_vehiculos():
    """Muestra los vehículos registrados."""

    if len(flota) == 0:
        print("\nNo hay vehículos registrados.")
        return

    print("\n" + "-" * 40)
    print("VEHÍCULOS REGISTRADOS")
    print("-" * 40)

    for i, vehiculo in enumerate(flota, start=1):
        estado = "Disponible" if vehiculo.disponible else "Alquilado"

        print(
            f"{i}. {vehiculo.marca} "
            f"{vehiculo.modelo} "
            f"({vehiculo.año}) - {estado}"
        )

    print("-" * 40)


def seleccionar_vehiculo():
    """Permite seleccionar un vehículo de la flota."""

    if len(flota) == 0:
        print("\nNo hay vehículos registrados.")
        return None

    mostrar_vehiculos()

    try:
        opcion = int(
            input("Selecciona el número del vehículo: ")
        )

        if opcion < 1 or opcion > len(flota):
            print("El número seleccionado no es válido.")
            return None

        return flota[opcion - 1]

    except ValueError:
        print("Debes introducir un número.")
        return None


def registrar_coche():
    """Registra un coche en la flota."""

    print("\n" + "-" * 50)
    print("             REGISTRAR COCHE")
    print("-" * 50)

    try:
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        año = int(input("Año: "))
        precio_base = float(input("Precio base por día: "))
        num_puertas = int(input("Número de puertas: "))

        if not Vehiculo.validar_año(año):
            print("El año no es válido.")
            return

        if not Vehiculo.validar_precio(precio_base):
            print("El precio base debe ser positivo.")
            return

        if num_puertas <= 0:
            print("El número de puertas debe ser positivo.")
            return

        coche = Coche(
            marca,
            modelo,
            año,
            precio_base,
            num_puertas
        )

        flota.append(coche)

        print("Coche agregado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def registrar_moto():
    """Registra una moto en la flota."""

    print("\n" + "-" * 50)
    print("             REGISTRAR MOTO")
    print("-" * 50)

    try:
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        año = int(input("Año: "))
        precio_base = float(input("Precio base por hora: "))
        cilindrada = int(input("Cilindrada en cc: "))

        if not Vehiculo.validar_año(año):
            print("El año no es válido.")
            return

        if not Vehiculo.validar_precio(precio_base):
            print("El precio base debe ser positivo.")
            return

        if cilindrada <= 0:
            print("La cilindrada debe ser positiva.")
            return

        moto = Moto(
            marca,
            modelo,
            año,
            precio_base,
            cilindrada
        )

        flota.append(moto)

        print("Moto agregada correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def mostrar_flota():
    """Muestra la información de todos los vehículos."""

    if len(flota) == 0:
        print("\nNo hay vehículos registrados.")
        return

    print("\n" + "-" * 50)
    print("              FLOTA DE VEHÍCULOS")
    print("-" * 50)

    for vehiculo in flota:
        vehiculo.mostrar_info()


def encender_apagar():
    """Enciende o apaga el motor de un vehículo."""

    vehiculo = seleccionar_vehiculo()

    if vehiculo is None:
        return

    print("\nEstado actual del motor:")

    if vehiculo.encendido:
        print("El motor está encendido.")
        opcion = input(
            "¿Deseas apagarlo? Escribe si: "
        ).strip().lower()

        if opcion == "si":
            vehiculo.apagar()
        else:
            print("Operación cancelada.")

    else:
        print("El motor está apagado.")
        opcion = input(
            "¿Deseas encenderlo? Escribe si: "
        ).strip().lower()

        if opcion == "si":
            vehiculo.encender()
        else:
            print("Operación cancelada.")


def calcular_alquiler():
    """Calcula el costo de alquiler de un vehículo."""

    vehiculo = seleccionar_vehiculo()

    if vehiculo is None:
        return

    if not vehiculo.disponible:
        print("No se puede calcular el alquiler.")
        print("El vehículo no está disponible.")
        return

    try:
        if isinstance(vehiculo, Coche):
            tiempo = float(
                input("¿Cuántos días deseas alquilarlo?: ")
            )

            costo = vehiculo.calcular_alquiler(tiempo)

            print(
                f"Costo de alquiler por {tiempo} días: "
                f"${costo:.2f}"
            )

        elif isinstance(vehiculo, Moto):
            tiempo = float(
                input("¿Cuántas horas deseas alquilarla?: ")
            )

            costo = vehiculo.calcular_alquiler(tiempo)

            print(
                f"Costo de alquiler por {tiempo} horas: "
                f"${costo:.2f}"
            )

    except ValueError as error:
        print(f"Error: {error}")


def alquilar_vehiculo():
    """Alquila un vehículo."""

    vehiculo = seleccionar_vehiculo()

    if vehiculo is None:
        return

    try:
        vehiculo.alquilar()

    except ValueError as error:
        print(f"Error: {error}")


def devolver_vehiculo():
    """Devuelve un vehículo alquilado."""

    vehiculo = seleccionar_vehiculo()

    if vehiculo is None:
        return

    try:
        vehiculo.devolver()

    except ValueError as error:
        print(f"Error: {error}")


def mostrar_estadisticas():
    """Muestra las estadísticas de la flota."""

    total = Vehiculo.total_vehiculos()

    encendidos = 0
    coches = 0
    motos = 0

    for vehiculo in flota:

        if vehiculo.encendido:
            encendidos += 1

        if isinstance(vehiculo, Coche):
            coches += 1

        elif isinstance(vehiculo, Moto):
            motos += 1

    print("\n" + "-" * 50)
    print("             ESTADÍSTICAS")
    print("-" * 50)
    print(f"Vehículos totales: {total}")
    print(f"Vehículos encendidos: {encendidos}")
    print(f"Coches: {coches}")
    print(f"Motos: {motos}")
    print("-" * 50)


def dar_de_baja():
    """Elimina un vehículo de la flota."""

    vehiculo = seleccionar_vehiculo()

    if vehiculo is None:
        return

    print(
        f"\n¿Deseas dar de baja a "
        f"{vehiculo.marca} {vehiculo.modelo}?"
    )

    confirmacion = input(
        "Escribe si para confirmar: "
    ).strip().lower()

    if confirmacion == "si":

        posicion = flota.index(vehiculo)

        vehiculo_eliminado = flota.pop(posicion)

        del vehiculo_eliminado

        print("Vehículo dado de baja correctamente.")

    else:
        print("Operación cancelada.")


def main():
    """Ejecuta el programa principal."""

    print("\n")
    print("-" * 50)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE VEHÍCULOS")
    print("-" * 50)

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        try:

            if opcion == "1":
                registrar_coche()

            elif opcion == "2":
                registrar_moto()

            elif opcion == "3":
                mostrar_flota()

            elif opcion == "4":
                encender_apagar()

            elif opcion == "5":
                calcular_alquiler()

            elif opcion == "6":
                alquilar_vehiculo()

            elif opcion == "7":
                devolver_vehiculo()

            elif opcion == "8":
                mostrar_estadisticas()

            elif opcion == "9":
                dar_de_baja()

            elif opcion == "10":
                print("\nGracias por utilizar el sistema.")
                print("Hasta pronto.")
                break

            else:
                print(
                    "Opción no válida. "
                    "Selecciona una opción del 1 al 10."
                )

        except IndexError:
            print("El vehículo seleccionado no existe.")

        except Exception as error:
            print(f"Ocurrió un error: {error}")


if __name__ == "__main__":
    main()