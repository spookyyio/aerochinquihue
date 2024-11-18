from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class VistaEncomiendas(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        header_label = QLabel("Agendar una encomienda")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        description_label = QLabel("Página para agendar encomiendas.")
        layout.addWidget(header_label)
        layout.addWidget(description_label)
