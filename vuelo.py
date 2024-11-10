class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, hora_salida, duracion, asientos_disponibles, precio_pasaje, precio_encomienda):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora_salida = hora_salida
        self.duracion = duracion
        self.asientos_disponibles = asientos_disponibles
        self.precio_pasaje = precio_pasaje
        self.precio_encomienda = precio_encomienda

    def reservar_asiento(self, cantidad=1):
        if self.asientos_disponibles >= cantidad:
            self.asientos_disponibles -= cantidad
            return True
        return False

    def cancelar_reserva(self, cantidad=1):
        self.asientos_disponibles += cantidad

    def mostrar_informacion(self):
        return (f"Vuelo {self.numero_vuelo}: {self.origen} -> {self.destino}\n"
                f"Fecha: {self.fecha} Hora de salida: {self.hora_salida}\n"
                f"Duración: {self.duracion} Asientos disponibles: {self.asientos_disponibles}\n"
                f"Precio Pasaje: ${self.precio_pasaje} Precio Encomienda: ${self.precio_encomienda}/kg")