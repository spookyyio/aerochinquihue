from vuelo import Vuelo

class ControladorVuelo:
    def _init_(self):
        self.vuelos = {}

    def agregar_vuelo(self, numero_vuelo, origen, destino, fecha, hora_salida, duracion, asientos_disponibles):
        vuelo = Vuelo(numero_vuelo, origen, destino, fecha, hora_salida, duracion, asientos_disponibles)
        self.vuelos[numero_vuelo] = vuelo

    def reservar_asiento(self, numero_vuelo, cantidad=1):
        if numero_vuelo in self.vuelos:
            return self.vuelos[numero_vuelo].reservar_asiento(cantidad)
        return False

    def mostrar_informacion_vuelo(self, numero_vuelo):
        if numero_vuelo in self.vuelos:
            return self.vuelos[numero_vuelo].mostrar_informacion()
        return "Vuelo no encontrado."