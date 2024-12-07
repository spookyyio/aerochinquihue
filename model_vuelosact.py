import csv
import os

class FlightVisualizerModel:
    def __init__(self, csv_file='vuelos.csv'):
        self.csv_file = csv_file

    def get_flights(self):
        flights = []
        if os.path.exists(self.csv_file) and os.path.getsize(self.csv_file) > 0:    # revisar si el archivo existe y no esta vacio
            with open(self.csv_file, mode='r', newline='') as file:    # abrir el archivo en modo lectura
                reader = csv.reader(file)   # leer el archivo
                for row in reader:  # recorrer el archivo
                    flights.append(row) # agregar los datos a la lista
        return flights  # retornar la lista