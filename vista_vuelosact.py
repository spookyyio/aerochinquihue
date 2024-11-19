from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QFormLayout, QScrollArea

class VistaVuelosAct(QWidget):
    def __init__(self):
        super().__init__()
        from controller_vuelosact import FlightVisualizer
        from model_vuelosact import FlightVisualizerModel
        self.controller = FlightVisualizer(FlightVisualizerModel())
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        header_label = QLabel("Vuelos actuales")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

        self.refresh_view()

    def refresh_view(self):
        # Clear existing flight boxes
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        flights = self.controller.get_flights()
        for flight in flights:
            flight_box = QGroupBox(f"Flight {flight[0]}")
            flight_layout = QFormLayout()
            flight_layout.addRow("Flight Number:", QLabel(flight[0]))
            flight_layout.addRow("Destination:", QLabel(flight[1]))
            flight_layout.addRow("Date:", QLabel(flight[2]))
            flight_box.setLayout(flight_layout)
            self.scroll_layout.addWidget(flight_box)