# model_agendar.py
import csv

class ModeloAgendarVuelo:
    def __init__(self, flights_csv='vuelos.csv', destinations_csv='destinations.csv', packages_csv='packages.csv', passwords_csv='passwords.csv'):
        self.flights_csv = flights_csv
        self.destinations_csv = destinations_csv
        self.packages_csv = packages_csv
        self.passwords_csv = passwords_csv

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

    def save_package(self, package_data):
        with open(self.packages_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(package_data)

    def get_packages(self):
        packages = []
        with open(self.packages_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                packages.append(row)
        return packages

    def get_passwords(self):
        passwords = {}
        with open(self.passwords_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                passwords[row[0]] = row[1]
        return passwords

    def get_flights_by_destination(self, destination):
        flights = []
        with open(self.flights_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == destination:
                    flights.append(row)
        flights.sort(key=lambda x: x[10])  # Sort by date
        return flights

    def remove_passenger(self, flight_data):
        flights = []
        with open(self.flights_csv, mode='r') as file:
            reader = csv.reader(file)
            flights = list(reader)
        with open(self.flights_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in flights:
                if row != flight_data:
                    writer.writerow(row)

    def add_passenger(self, flight_data):
        self.save_flight(flight_data)

    def get_current_bookings(self, destination, date):
        current_cargo = 0
        current_passengers = 0
        with open(self.flights_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == destination and row[10] == date:
                    current_passengers += 1
                    if row[7] == 'True':  # Package checkbox is checked
                        current_cargo += float(row[8])
        return current_cargo, current_passengers

    def get_packages_by_destination(self, destination):
        packages = []
        with open(self.packages_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == destination:
                    packages.append(row)
        return packages

    def remove_package(self, package_data):
        packages = []
        with open(self.packages_csv, mode='r') as file:
            reader = csv.reader(file)
            packages = list(reader)
        with open(self.packages_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in packages:
                if row != package_data:
                    writer.writerow(row)

    def add_package(self, package_data):
        self.save_package(package_data)