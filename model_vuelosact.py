import csv

class FlightVisualizerModel:
    def __init__(self, csv_file='vuelos.csv'):
        self.csv_file = csv_file

    def get_flights(self):
        flights = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                flights.append(row)
        return flights