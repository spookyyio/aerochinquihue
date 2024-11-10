# controlador_vuelo.py
from vuelo import Vuelo
from datos_vuelos import datos_vuelos

class ControladorVuelo:
    def __init__(self):
        self.vuelos = {}

    def poblar_vuelos(self):
        for datos in datos_vuelos:
            vuelo = Vuelo(
                datos["numero_vuelo"],
                datos["origen"],
                datos["destino"],
                datos["fecha"],
                datos["hora_salida"],
                datos["duracion"],
                datos["asientos_disponibles"],
                datos["precio_pasaje"],
                datos["precio_encomienda"]
            )
            self.vuelos[vuelo.numero_vuelo] = vuelo

    def mostrar_vuelos(self):
        for vuelo in self.vuelos.values():
            print(vuelo.mostrar_informacion())
            print("-" * 30)  # Separador entre vuelos
