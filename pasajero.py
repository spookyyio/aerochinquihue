class Pasajero:
    def __init__(self, id_pasajero, nombre, apellido, pasaporte, nacionalidad, edad):
        self.id_pasajero = id_pasajero
        self.nombre = nombre
        self.apellido = apellido
        self.pasaporte = pasaporte
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.vuelos_reservados = []  # Lista de vuelos reservados por el pasajero

    def agregar_reserva(self, vuelo):
        self.vuelos_reservados.append(vuelo)

    def cancelar_reserva(self, vuelo):
        if vuelo in self.vuelos_reservados:
            self.vuelos_reservados.remove(vuelo)

    def mostrar_informacion(self):
        return (f"ID Pasajero: {self.id_pasajero}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Pasaporte: {self.pasaporte}\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Edad: {self.edad}\n"
                f"Vuelos reservados: {[vuelo.numero_vuelo for vuelo in self.vuelos_reservados]}")