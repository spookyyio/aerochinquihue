# vista_agendar.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QComboBox

class VistaAgendar(QWidget):
    def __init__(self, controller, vuelos_act_view):
        super().__init__()
        self.controller = controller
        self.vuelos_act_view = vuelos_act_view
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        form_layout = QFormLayout()
        
        self.destination_combo = QComboBox()
        destinations = self.controller.get_destinations()
        for destination in destinations:
            self.destination_combo.addItem(destination[0], destination)
        
        self.client_name_input = QLineEdit()
        self.package_input = QLineEdit()
        
        form_layout.addRow("Destination:", self.destination_combo)
        form_layout.addRow("Client Name:", self.client_name_input)
        form_layout.addRow("Package (Y/N):", self.package_input)
        
        layout.addLayout(form_layout)
        
        schedule_button = QPushButton("Schedule Flight")
        schedule_button.clicked.connect(self.schedule_flight)
        layout.addWidget(schedule_button)

    def schedule_flight(self):
        selected_destination = self.destination_combo.currentData()
        flight_data = [
            selected_destination[0],  # Destination
            selected_destination[1],  # Aircraft
            selected_destination[2],  # Departure Time
            selected_destination[3],  # Landing Time
            selected_destination[4],  # Max Cargo
            selected_destination[5],  # Max Passengers
            self.client_name_input.text(),  # Client Name
            self.package_input.text()  # Package
        ]
        self.controller.schedule_flight(flight_data)
        self.vuelos_act_view.refresh_view()