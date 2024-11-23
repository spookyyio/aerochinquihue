# vista_admin.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QComboBox, QMessageBox, QInputDialog
from controller_agendar import FlightSchedulerController

class VistaAdmin(QWidget):
    def __init__(self, controller, vuelos_act_view):
        super().__init__()
        self.controller = controller
        self.vuelos_act_view = vuelos_act_view
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        header_label = QLabel("Administrar vuelos")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        description_label = QLabel("Página para administrar vuelos")
        layout.addWidget(header_label)
        layout.addWidget(description_label)

        self.password_input, ok = QInputDialog.getText(self, 'Contraseña', 'Ingrese la contraseña:', QLineEdit.EchoMode.Password)
        if not ok:
            return

        passwords = self.controller.get_passwords()
        if self.password_input not in passwords.values():
            QMessageBox.warning(self, "Error", "Contraseña incorrecta.")
            return

        self.role = [role for role, password in passwords.items() if password == self.password_input][0]

        self.destination_combo = QComboBox()
        destinations = self.controller.get_destinations()
        for destination in destinations:
            self.destination_combo.addItem(destination[0], destination)
        self.destination_combo.currentIndexChanged.connect(self.update_flights)

        self.flights_combo = QComboBox()
        self.flights_combo.currentIndexChanged.connect(self.show_flight_details)

        layout.addWidget(QLabel("Seleccionar destino:"))
        layout.addWidget(self.destination_combo)
        layout.addWidget(QLabel("Seleccionar vuelo:"))
        layout.addWidget(self.flights_combo)

        self.flight_details_label = QLabel()
        layout.addWidget(self.flight_details_label)

        self.add_passenger_button = QPushButton("Agregar pasajero")
        self.add_passenger_button.clicked.connect(self.add_passenger)
        layout.addWidget(self.add_passenger_button)

        self.remove_passenger_button = QPushButton("Eliminar pasajero")
        self.remove_passenger_button.clicked.connect(self.remove_passenger)
        layout.addWidget(self.remove_passenger_button)

        self.setLayout(layout)

    def update_flights(self):
        self.flights_combo.clear()
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            flights = self.controller.get_flights_by_destination(selected_destination[0])
            for flight in flights:
                self.flights_combo.addItem(flight[10], flight)

    def show_flight_details(self):
        selected_flight = self.flights_combo.currentData()
        if selected_flight:
            details = f"Destino: {selected_flight[0]}\nAeronave: {selected_flight[1]}\nHora de salida: {selected_flight[2]}\nHora de llegada: {selected_flight[3]}\nCarga máxima: {selected_flight[4]} kg\nPasajeros máximos: {selected_flight[5]}\nNombre del cliente: {selected_flight[6]}\nPaquete: {selected_flight[7]}\nPeso del paquete: {selected_flight[8]}\nDimensiones del paquete: {selected_flight[9]}\nFecha: {selected_flight[10]}"
            self.flight_details_label.setText(details)

    def add_passenger(self):
        if self.role != "BOSS":
            QMessageBox.warning(self, "Error", "Solo el BOSS puede agregar un pasajero.")
            return

        passenger_name, ok = QInputDialog.getText(self, 'Agregar pasajero', 'Ingrese el nombre del pasajero:')
        if not ok:
            return

        selected_flight = self.flights_combo.currentData()
        if selected_flight:
            flight_data = selected_flight.copy()
            flight_data[6] = passenger_name  # Update client name
            self.controller.add_passenger(flight_data)
            self.update_flights()
            self.vuelos_act_view.refresh_view()

    def remove_passenger(self):
        if self.role != "BOSS":
            QMessageBox.warning(self, "Error", "Solo el BOSS puede eliminar un pasajero.")
            return

        selected_flight = self.flights_combo.currentData()
        if selected_flight:
            self.controller.remove_passenger(selected_flight)
            self.update_flights()
            self.vuelos_act_view.refresh_view()