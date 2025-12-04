from PyQt5.QtWidgets import (
     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
     QLabel, QPushButton, QLineEdit, QTextEdit, QMainWindow, QInputDialog
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets
import sys

import matplotlib.pyplot as plt
import io

class FormProduct:
    def __init__(self):
        self.layout = QVBoxLayout()

    def add_widget(self, widget):
        self.layout.addWidget(widget)

class FormDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_form(self):
        self.builder.add_title()
        self.builder.add_inputs()
        self.builder.add_controls()
        return self.builder.get_result()

class AddTitle(QMainWindow):
    def __init__(self):
        super().__init__()

class AddInput(QPushButton):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Enter Details", self)
        self.button.setGeometry(80, 80, 140, 40)
        self.button.clicked.connect(self.show_input_dialog)
        self.setWindowTitle("3 вариант, первое задание, паттерны")
        self.setGeometry(200, 200, 600, 400)

class AddControls(QPushButton):
    def __init__(self):
        super().__init__()
        button = QPushButton('Нажми сюда', self)
        button.setToolTip('Это кнопка')
        button.move(100, 70)
        button.clicked.connect(self.on_click)



class MainWindow(AddTitle, AddInput, AddControls, FormDirector):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())