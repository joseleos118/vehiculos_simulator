from datetime import datetime


class Vehiculo:
    _contador_vehiculos = 0

    def __init__(self, marca, modelo, año, precio_base):
        if not self.validar_año(año):
            raise ValueError("El año no es válido.")

        if not self.validar_precio(precio_base):
            raise ValueError("El precio base debe ser positivo.")

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base

        self._encendido = False
        self._disponible = True

        Vehiculo._contador_vehiculos += 1

        print(
            f"Vehículo registrado: {self.marca} "
            f"{self.modelo} ({self.año})"
        )

    def __del__(self):
        """Da de baja el vehículo y actualiza el contador."""

        try:
            Vehiculo._contador_vehiculos -= 1
            print(
                f"{self.marca} {self.modelo} "
                "ha sido dado de baja."
            )
        except AttributeError:
            pass

    def encender(self):
        """Enciende el motor del vehículo."""

        if not self._encendido:
            self._encendido = True
            print(
                f"{self.marca} {self.modelo}: "
                "Motor encendido."
            )
        else:
            print("El motor ya está encendido.")

    def apagar(self):
        """Apaga el motor del vehículo."""

        if self._encendido:
            self._encendido = False
            print(
                f"{self.marca} {self.modelo}: "
                "Motor apagado."
            )
        else:
            print("El motor ya está apagado.")

    def calcular_alquiler(self, tiempo):
        """Calcula el costo de alquiler."""

        raise NotImplementedError(
            "Este método debe redefinirse en la clase derivada."
        )

    def mostrar_info(self):
        """Muestra la información del vehículo."""

        estado_motor = "Encendido" if self._encendido else "Apagado"
        disponibilidad = (
            "Disponible" if self._disponible else "Alquilado"
        )

        print("\n" + "-" * 40)
        print("INFORMACIÓN DEL VEHÍCULO")
        print("-" * 40)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio base: ${self.precio_base}")
        print(f"Motor: {estado_motor}")
        print(f"Disponibilidad: {disponibilidad}")
        print("-" * 40)

    def alquilar(self):
        """Marca el vehículo como no disponible."""

        if not self._disponible:
            raise ValueError("El vehículo ya está alquilado.")

        self._disponible = False
        print(
            f"{self.marca} {self.modelo} "
            "ha sido alquilado."
        )

    def devolver(self):
        """Marca el vehículo como disponible."""

        if self._disponible:
            raise ValueError("El vehículo no está alquilado.")

        self._disponible = True
        print(
            f"{self.marca} {self.modelo} "
            "ha sido devuelto."
        )

    @classmethod
    def total_vehiculos(cls):
        """Devuelve el total de vehículos activos."""

        return cls._contador_vehiculos

    @classmethod
    def crear_desde_diccionario(cls, datos):
        """Crea un vehículo usando un diccionario."""

        return cls(
            datos["marca"],
            datos["modelo"],
            datos["año"],
            datos["precio_base"]
        )

    @staticmethod
    def validar_año(año):
        """Valida que el año sea válido."""

        año_actual = datetime.now().year

        return (
            isinstance(año, int)
            and año > 1900
            and año <= año_actual
        )

    @staticmethod
    def validar_precio(precio):
        """Valida que el precio sea positivo."""

        return (
            isinstance(precio, (int, float))
            and precio > 0
        )

    @property
    def encendido(self):
        """Devuelve el estado del motor."""

        return self._encendido

    @property
    def disponible(self):
        """Devuelve la disponibilidad del vehículo."""

        return self._disponible


class Coche(Vehiculo):

    def __init__(
        self,
        marca,
        modelo,
        año,
        precio_base,
        num_puertas
    ):
        super().__init__(
            marca,
            modelo,
            año,
            precio_base
        )

        if not isinstance(num_puertas, int) or num_puertas <= 0:
            raise ValueError(
                "El número de puertas debe ser un entero positivo."
            )

        self.num_puertas = num_puertas

    def calcular_alquiler(self, dias):
        """Calcula el costo de alquiler del coche."""

        if not isinstance(dias, (int, float)) or dias <= 0:
            raise ValueError(
                "Los días deben ser un número positivo."
            )

        return self.precio_base * dias + (self.num_puertas * 10)

    def mostrar_info(self):
        """Muestra la información del coche."""

        super().mostrar_info()
        print(f"Puertas: {self.num_puertas}")

    def abrir_maletero(self):
        """Abre el maletero del coche."""

        print(
            f"{self.marca} {self.modelo}: "
            "Maletero abierto."
        )


class Moto(Vehiculo):

    def __init__(
        self,
        marca,
        modelo,
        año,
        precio_base,
        cilindrada
    ):
        super().__init__(
            marca,
            modelo,
            año,
            precio_base
        )

        if not isinstance(cilindrada, int) or cilindrada <= 0:
            raise ValueError(
                "La cilindrada debe ser un entero positivo."
            )

        self.cilindrada = cilindrada

    def calcular_alquiler(self, horas):
        """Calcula el costo de alquiler de la moto."""

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ValueError(
                "Las horas deben ser un número positivo."
            )

        return self.precio_base * horas + (
            self.cilindrada * 0.5
        )

    def mostrar_info(self):
        """Muestra la información de la moto."""

        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada} cc")

    def hacer_caballito(self):
        """Muestra la acción de hacer un caballito."""

        print(
            f"{self.marca} {self.modelo}: "
            "Haciendo caballito."
        )