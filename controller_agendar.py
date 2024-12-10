from model_agendar import ModeloAgendarVuelo
import csv

class FlightSchedulerController:
    def __init__(self, model):
        self.model = model

    def schedule_flight(self, flight_data):
        self.model.save_flight(flight_data)

    def get_destinations(self):
        return self.model.get_destinations()

    def save_package(self, package_data):
        self.model.save_package(package_data)

    def get_packages(self):
        return self.model.get_packages()

    def get_passwords(self):
        return self.model.get_passwords()

    def get_flights_by_destination(self, destination):
        return self.model.get_flights_by_destination(destination)

    def remove_package(self, package_data):
        packages = []
        with open('packages.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            packages = [row for row in reader if row != package_data]

        with open('packages.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(packages)

    def add_passenger(self, flight_data):
        self.model.add_passenger(flight_data)

    def get_current_bookings(self, destination, date):
        return self.model.get_current_bookings(destination, date)

    def get_packages_by_destination(self, destination):
        return self.model.get_packages_by_destination(destination)

    def get_all_flights(self):
        return self.model.get_all_flights()

    def remove_flight(self, flight_data):
        self.model.remove_flight(flight_data)