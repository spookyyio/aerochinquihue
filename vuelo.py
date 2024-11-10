class Vuelo:
    def __init__(self, flightID, origen, destino, fecha, hora_salida, duracion, asientos_disp, precio):
        self.flightID = flightID
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora_salida = hora_salida
        self.duracion = duracion
        self.asientos_disp = asientos_disp
        self.precio = precio

    def reservar_asientos(self, cantidad):
        if self.asientos_disp >= cantidad:
            self.asientos_disp -= cantidad
            return True
        return False

    def cancelar_reserva(self, cantidad):
        self.asientos_disp += cantidad

    def mostrar_info(self):
        print(f"Vuelo {self.flightID} de {self.origen} a {self.destino} el {self.fecha} a las {self.hora_salida}. Duración: {self.duracion}. Asientos disponibles: {self.asientos_disp}. Precio: {self.precio}")