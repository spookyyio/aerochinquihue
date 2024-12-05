# vista_adminvuelos.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import QDate
from controller_agendar import FlightSchedulerController

class VistaAdminVuelos(QWidget):
    def __init__(self, controller, vuelos_act_view):
        super().__init__()
        self.controller = controller
        self.vuelos_act_view = vuelos_act_view
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        form_layout = QFormLayout()
        
        self.flights_combo = QComboBox()
        self.update_flights()
        
        form_layout.addRow("Vuelos:", self.flights_combo)
        
        layout.addLayout(form_layout)
        
        delete_flight_button = QPushButton("Eliminar vuelo")
        delete_flight_button.clicked.connect(self.delete_flight)
        layout.addWidget(delete_flight_button)
        
        self.setLayout(layout)

    def update_flights(self):
        self.flights_combo.clear()
        flights = self.controller.get_all_flights()
        for flight in flights:
            flight_info = f"{flight[0]} - {flight[1]} - {flight[2]} - {flight[3]} - {flight[10]}"
            self.flights_combo.addItem(flight_info, flight)

    def delete_flight(self):
        selected_flight = self.flights_combo.currentData()
        if selected_flight:
            self.controller.remove_flight(selected_flight)
            self.update_flights()
            self.vuelos_act_view.refresh_view()
            QMessageBox.information(self, "Éxito", "Vuelo eliminado exitosamente.")