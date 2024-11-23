# vista_adminpackages.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QComboBox, QMessageBox, QInputDialog
from controller_agendar import FlightSchedulerController

class VistaAdminPackages(QWidget):
    def __init__(self, controller, vuelos_act_view):
        super().__init__()
        self.controller = controller
        self.vuelos_act_view = vuelos_act_view
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        header_label = QLabel("Administrar paquetes")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        description_label = QLabel("Página para administrar paquetes")
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
        self.destination_combo.currentIndexChanged.connect(self.update_packages)

        self.packages_combo = QComboBox()
        self.packages_combo.currentIndexChanged.connect(self.show_package_details)

        layout.addWidget(QLabel("Seleccionar destino:"))
        layout.addWidget(self.destination_combo)
        layout.addWidget(QLabel("Seleccionar paquete:"))
        layout.addWidget(self.packages_combo)

        self.package_details_label = QLabel()
        layout.addWidget(self.package_details_label)

        self.add_package_button = QPushButton("Agregar paquete")
        self.add_package_button.clicked.connect(self.add_package)
        layout.addWidget(self.add_package_button)

        self.remove_package_button = QPushButton("Eliminar paquete")
        self.remove_package_button.clicked.connect(self.remove_package)
        layout.addWidget(self.remove_package_button)

        self.setLayout(layout)

    def update_packages(self):
        self.packages_combo.clear()
        selected_destination = self.destination_combo.currentData()
        if selected_destination:
            packages = self.controller.get_packages_by_destination(selected_destination[0])
            for package in packages:
                self.packages_combo.addItem(package[2], package)

    def show_package_details(self):
        selected_package = self.packages_combo.currentData()
        if selected_package:
            details = f"Destino: {selected_package[0]}\nNombre del cliente: {selected_package[1]}\nPeso del paquete: {selected_package[2]}\nDimensiones del paquete: {selected_package[3]}\nFecha: {selected_package[4]}"
            self.package_details_label.setText(details)

    def add_package(self):
        if self.role != "BOSS":
            QMessageBox.warning(self, "Error", "Solo el BOSS puede agregar un paquete.")
            return

        package_name, ok = QInputDialog.getText(self, 'Agregar paquete', 'Ingrese el nombre del paquete:')
        if not ok:
            return

        selected_package = self.packages_combo.currentData()
        if selected_package:
            package_data = selected_package.copy()
            package_data[1] = package_name  # Update package name
            self.controller.add_package(package_data)
            self.update_packages()
            self.vuelos_act_view.refresh_view()

    def remove_package(self):
        if self.role != "BOSS":
            QMessageBox.warning(self, "Error", "Solo el BOSS puede eliminar un paquete.")
            return

        selected_package = self.packages_combo.currentData()
        if selected_package:
            self.controller.remove_package(selected_package)
            self.update_packages()
            self.vuelos_act_view.refresh_view()