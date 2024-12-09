from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QLineEdit, QCheckBox, QDateEdit, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import QDate, pyqtSignal

class VistaAgendar(QWidget):
    reservation_made = pyqtSignal(list)

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
        self.destination_combo.currentIndexChanged.connect(self.update_max_cargo) # actualiza la cantidad de peso segun el viaje seleccionado en la lista
        
        self.client_name_input = QLineEdit()
        self.package_checkbox = QCheckBox("Paquete")
        self.package_checkbox.stateChanged.connect(self.toggle_package_fields)
        self.package_weight_input = QLineEdit()
        self.package_dimensions_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.max_cargo_label = QLabel("Carga máxima: ")
        
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
        
        schedule_button = QPushButton("Agendar vuelo")
        schedule_button.clicked.connect(self.schedule_flight)
        layout.addWidget(schedule_button)
        
        self.setLayout(layout)

    def update_max_cargo(self):
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            self.max_cargo_label.setText(f"Carga máxima: {selected_destination[4]} kg")

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
                QMessageBox.warning(self, "Error", "El vuelo ya ha alcanzado el número máximo de pasajeros.")
                return

            if current_cargo + package_weight > max_cargo:
                QMessageBox.warning(self, "Error", "El peso del paquete excede la capacidad máxima de carga del avión.")
                return

            base_price = float(selected_destination[6])
            package_price = float(selected_destination[7]) if self.package_checkbox.isChecked() else 0
            total_price = base_price + package_price

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
                date,
                total_price  # precio total incluyendo el precio del paquete
            ]
            self.controller.schedule_flight(flight_data) # llama al controlador y entrega los datos
            self.vuelos_act_view.refresh_view() # refresca la vista de vuelos actuales
            self.reservation_made.emit(flight_data) # emite la señal de que se ha hecho una reserva