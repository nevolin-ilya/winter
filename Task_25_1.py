import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Begin!")
        self.setWindowTitle("Count")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.count = 1
    def the_button_was_clicked(self):
        # if self.count == 0:
        #     self.button.setText("Begin")
        # else:
        self.button.setText(f"{self.count}")
        self.count = 1 + self.count


app = QApplication([])
window = MainWindow()
window.show()
app.exec()