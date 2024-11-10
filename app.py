import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

if __name__ == '__main__':

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Aero Chinquihue")
            self.setFixedSize(QSize(400, 300))

            button = QPushButton("Click me")
            button.setCheckable(True)
            button.clicked.connect(self.on_button_clicked)
            button.clicked.connect(self.on_button_toggled)

            self.setCentralWidget(button)

        def on_button_clicked(self):
            print("CLICK!")
        def on_button_toggled(self,checked):
            print("Checked?", checked)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  


    app.exec()
