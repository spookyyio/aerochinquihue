# vista_encomiendas.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QComboBox, QMessageBox
from PyQt6.QtCore import QDate
from controller_agendar import FlightSchedulerController

class VistaEncomiendas(QWidget):
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
        self.package_weight_input = QLineEdit()
        self.package_dimensions_input = QLineEdit()
        self.current_date_input = QLineEdit()
        self.current_date_input.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        self.current_date_input.setReadOnly(True)
        self.max_cargo_label = QLabel("Carga Maxima: ")
        
        form_layout.addRow("Destino:", self.destination_combo)
        form_layout.addRow("Nombre del Cliente:", self.client_name_input)
        form_layout.addRow("Peso del paquete:", self.package_weight_input)
        form_layout.addRow("Dimensiones del paquete:", self.package_dimensions_input)
        form_layout.addRow("Fecha actual:", self.current_date_input)
        form_layout.addRow(self.max_cargo_label)
        
        layout.addLayout(form_layout)
        
        create_package_button = QPushButton("Crear Encomienda")
        create_package_button.clicked.connect(self.create_package)
        layout.addWidget(create_package_button)

    def update_max_cargo(self):
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            self.max_cargo_label.setText(f"Carga Maxima: {selected_destination[4]} kg")

    def create_package(self):
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            max_cargo = float(selected_destination[4])
            package_weight = float(self.package_weight_input.text()) if self.package_weight_input.text() else 0
            date = self.current_date_input.text()
            current_cargo, _ = self.controller.get_current_bookings(selected_destination[0], date)
            
            if current_cargo + package_weight > max_cargo:
                QMessageBox.warning(self, "Error", "El paquete excede la carga maxima.")
                return

            package_data = [
                selected_destination[0],  
                self.client_name_input.text(),  
                self.package_weight_input.text(),  
                self.package_dimensions_input.text(), 
                date  
            ]
            self.controller.save_package(package_data)
            self.vuelos_act_view.refresh_view()