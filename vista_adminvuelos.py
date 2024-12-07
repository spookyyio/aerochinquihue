# vista_adminvuelos.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import QDate
from controller_agendar import FlightSchedulerController

class VistaAdminVuelos(QWidget):
    def __init__(self, controller, vuelos_act_view):    # se inicializa la vista
        super().__init__()
        self.controller = controller    # se asigna el controlador
        self.vuelos_act_view = vuelos_act_view  # se asigna la vista de vuelos actuales
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)  # se crea un layout vertical
        
        form_layout = QFormLayout() # se crea un layout de formulario
        
        self.flights_combo = QComboBox()    # se crea un combobox para los vuelos
        self.update_flights()   # se actualizan los vuelos
        
        form_layout.addRow("Vuelos:", self.flights_combo)
        
        layout.addLayout(form_layout)
        
        delete_flight_button = QPushButton("Eliminar vuelo")
        delete_flight_button.clicked.connect(self.delete_flight)    # se conecta el boton a la funcion delete_flight
        layout.addWidget(delete_flight_button) # se agrega el boton al layout
        
        self.setLayout(layout)

    def update_flights(self): # funcion para actualizar los vuelos
        self.flights_combo.clear()
        flights = self.controller.get_all_flights() # se obtienen todos los vuelos
        for flight in flights:
            flight_info = f"{flight[0]} - {flight[1]} - {flight[2]} - {flight[3]} - {flight[10]}" # se obtiene la informacion del vuelo en esas posiciones
            self.flights_combo.addItem(flight_info, flight)

    def delete_flight(self):
        selected_flight = self.flights_combo.currentData()  # se obtiene el vuelo seleccionado
        if selected_flight:
            self.controller.remove_flight(selected_flight)  # se elimina el vuelo
            self.update_flights()   # se actualizan los vuelos
            self.vuelos_act_view.refresh_view()     # se refresca la vista de vuelos actuales
            QMessageBox.information(self, "Éxito", "Vuelo eliminado exitosamente.") #   se muestra un mensaje de exito