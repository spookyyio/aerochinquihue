import csv

class ModeloAgendarVuelo:
    def __init__(self, flights_csv='vuelos.csv', destinations_csv='destinations.csv'):
        self.flights_csv = flights_csv
        self.destinations_csv = destinations_csv

    def save_flight(self, flight_data):
        with open(self.flights_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(flight_data)

    def get_destinations(self):
        destinations = []
        with open(self.destinations_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                destinations.append(row)
        return destinations