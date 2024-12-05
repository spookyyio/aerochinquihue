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
        try:
            with open(self.destinations_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    destinations.append(row)
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return destinations

    def save_package(self, package_data):
        with open(self.packages_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(package_data)

    def get_packages(self):
        packages = []
        try:
            with open(self.packages_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    packages.append(row)
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return packages

    def get_passwords(self):
        passwords = {}
        try:
            with open(self.passwords_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    passwords[row[0]] = row[1]
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return passwords

    def get_flights_by_destination(self, destination):
        flights = []
        try:
            with open(self.flights_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == destination:
                        flights.append(row)
            flights.sort(key=lambda x: x[10])  # Sort by date
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return flights

    def get_current_bookings(self, destination, date):
        current_cargo = 0
        current_passengers = 0
        try:
            with open(self.flights_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == destination and row[10] == date:
                        current_passengers += 1
                        if row[7] == 'True':  # Package checkbox is checked
                            current_cargo += float(row[8])
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return current_cargo, current_passengers

    def get_packages_by_destination(self, destination):
        packages = []
        try:
            with open(self.packages_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == destination:
                        packages.append(row)
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return packages

    def remove_package(self, package_data):
        packages = []
        try:
            with open(self.packages_csv, mode='r') as file:
                reader = csv.reader(file)
                packages = list(reader)
            with open(self.packages_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in packages:
                    if row != package_data:
                        writer.writerow(row)
        except FileNotFoundError:
            pass

    def add_package(self, package_data):
        self.save_package(package_data)

    def get_all_flights(self):
        flights = []
        try:
            with open(self.flights_csv, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    flights.append(row)
        except StopIteration:
            pass
        except FileNotFoundError:
            pass
        return flights

    def remove_flight(self, flight_data):
        flights = []
        try:
            with open(self.flights_csv, mode='r') as file:
                reader = csv.reader(file)
                flights = list(reader)
            with open(self.flights_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in flights:
                    if row != flight_data:
                        writer.writerow(row)
        except FileNotFoundError:
            pass