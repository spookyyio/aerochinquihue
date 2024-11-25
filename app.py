## integrantes del equipo Kassandra Fuentes, Felipe Sanchez

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QStackedWidget, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from vista_agendar import VistaAgendar
from vista_encomiendas import VistaEncomiendas
from vista_vuelosact import VistaVuelosAct
from vista_admin import VistaAdmin
from vista_adminpackages import VistaAdminPackages
from controller_agendar import FlightSchedulerController
from model_agendar import ModeloAgendarVuelo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aero Chinquihue")
        self.setGeometry(100, 100, 1000, 600)

        self.navigation_buttons = {
            "AGENDAR UN VUELO": 0,
            "ENCOMIENDAS": 1,
            "VUELOS ACTUALES": 2,
            "[ADMIN] ADMINISTRAR VUELOS": 3,
            "[ADMIN] ADMINISTRAR PAQUETES": 4,
        }

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        self.button_widget = self.create_buttons()
        main_layout.addWidget(self.button_widget, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.stacked_widget = QStackedWidget()
        self.vuelos_act_view = VistaVuelosAct()
        pages = self.load_pages()
        for page in pages:
            self.stacked_widget.addWidget(page)
        main_layout.addWidget(self.stacked_widget)
        
        self.change_page(0)

    def create_buttons(self):
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)

        button_widget.setStyleSheet("background-color: #d3d3d3; padding: 20px; border-radius: 10px;")
        button_layout.setSpacing(20) 
        button_layout.setContentsMargins(10, 10, 10, 10)  

        for text, index in self.navigation_buttons.items():
            button = QPushButton(text)
            button.setStyleSheet("border-radius: 10px; padding: 10px; font-size: 14px;")
            button.clicked.connect(lambda _, idx=index: self.change_page(idx))
            button_layout.addWidget(button)

        return button_widget

    def load_pages(self):
        model = ModeloAgendarVuelo()
        controller = FlightSchedulerController(model)
        vista_agendar = VistaAgendar(controller, self.vuelos_act_view)
        vista_agendar.reservation_made.connect(self.handle_reservation_made)
        vista_encomiendas = VistaEncomiendas(controller, self.vuelos_act_view)
        vista_admin = VistaAdmin(controller, self.vuelos_act_view)
        vista_adminpackages = VistaAdminPackages(controller, self.vuelos_act_view)
        return [
            vista_agendar,
            vista_encomiendas,
            self.vuelos_act_view,
            vista_admin,
            vista_adminpackages,
        ]

    def change_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        for button in self.button_widget.findChildren(QPushButton):
            button.setStyleSheet("font-weight: normal;")
        self.button_widget.findChildren(QPushButton)[index].setStyleSheet("font-weight: bold;")

    def handle_reservation_made(self, flight_data):
        print("Nueva reserva realizada:", flight_data)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())