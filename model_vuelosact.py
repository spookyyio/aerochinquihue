import csv
import os

class FlightVisualizerModel:
    def __init__(self, csv_file='vuelos.csv'):
        self.csv_file = csv_file

    def get_flights(self):
        flights = []
        if os.path.exists(self.csv_file) and os.path.getsize(self.csv_file) > 0:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    flights.append(row)
        return flights