from pasajero import Pasajero
from vuelo import Vuelo

class ControladorPasajero:
    def __init__(self):
        self.pasajeros = {}

    def agregar_pasajero(self, id_pasajero, nombre, apellido, pasaporte, nacionalidad, edad):
        pasajero = Pasajero(id_pasajero, nombre, apellido, pasaporte, nacionalidad, edad)
        self.pasajeros[id_pasajero] = pasajero

    def reservar_vuelo(self, id_pasajero, vuelo):
        if id_pasajero in self.pasajeros:
            self.pasajeros[id_pasajero].agregar_reserva(vuelo)
            return True
        return False

    def cancelar_reserva(self, id_pasajero, vuelo):
        if id_pasajero in self.pasajeros:
            self.pasajeros[id_pasajero].cancelar_reserva(vuelo)
            return True
        return False

    def mostrar_informacion_pasajero(self, id_pasajero):
        if id_pasajero in self.pasajeros:
            return self.pasajeros[id_pasajero].mostrar_informacion()
        return "Pasajero no encontrado."