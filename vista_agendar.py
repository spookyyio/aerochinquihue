# vista_agendar.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QComboBox, QCheckBox, QDateEdit, QMessageBox
from PyQt6.QtCore import pyqtSignal, QDate, Qt

class VistaAgendar(QWidget):
    reservation_made = pyqtSignal(list)  # Define a custom signal

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
        self.destination_combo.currentIndexChanged.connect(self.update_max_cargo)
        
        self.client_name_input = QLineEdit()
        self.package_checkbox = QCheckBox("Paquete?")
        self.package_checkbox.stateChanged.connect(self.toggle_package_fields)
        self.package_weight_input = QLineEdit()
        self.package_dimensions_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.max_cargo_label = QLabel("Carga Maxima:")
        
        self.package_weight_input.setEnabled(False)
        self.package_dimensions_input.setEnabled(False)
        
        form_layout.addRow("Destino:", self.destination_combo)
        form_layout.addRow("Nombre del cliente:", self.client_name_input)
        form_layout.addRow("Paquete:", self.package_checkbox)
        form_layout.addRow("Peso del paquete:", self.package_weight_input)
        form_layout.addRow("Dimensiones del paquete:", self.package_dimensions_input)
        form_layout.addRow("Fecha:", self.date_input)
        form_layout.addRow(self.max_cargo_label)
        
        layout.addLayout(form_layout)
        
        schedule_button = QPushButton("Agendar Vuelo")
        schedule_button.clicked.connect(self.schedule_flight)
        layout.addWidget(schedule_button)

    def update_max_cargo(self):
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            self.max_cargo_label.setText(f"Max Cargo: {selected_destination[4]} kg")

    def toggle_package_fields(self, state):
        if state == 2:
            self.package_weight_input.setEnabled(True)
            self.package_dimensions_input.setEnabled(True)
        else:
            self.package_weight_input.setEnabled(False)
            self.package_dimensions_input.setEnabled(False)

    def schedule_flight(self):
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            max_cargo = float(selected_destination[4])
            max_passengers = int(selected_destination[5])
            package_weight = float(self.package_weight_input.text()) if self.package_weight_input.text() else 0
            date = self.date_input.date().toString("yyyy-MM-dd")
            current_cargo, current_passengers = self.controller.get_current_bookings(selected_destination[0], date)
            
            if current_passengers >= max_passengers:
                QMessageBox.warning(self, "Error", "El vuelo ya está lleno.")
                return

            if current_cargo + package_weight > max_cargo:
                QMessageBox.warning(self, "Error", "El paquete excede la capacidad de carga máxima del avión.")
                return

            flight_data = [
                selected_destination[0],  
                selected_destination[1],  
                selected_destination[2],  
                selected_destination[3],  
                selected_destination[4],  
                selected_destination[5],  
                self.client_name_input.text(),  
                self.package_checkbox.isChecked(),  
                self.package_weight_input.text(),
                self.package_dimensions_input.text(),  
                date  # Date
            ]
            self.controller.schedule_flight(flight_data)
            self.vuelos_act_view.refresh_view()
            self.reservation_made.emit(flight_data) 