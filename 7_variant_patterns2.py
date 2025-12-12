from PyQt5.QtWidgets import (
     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
     QLabel, QPushButton, QLineEdit, QComboBox, QGridLayout, QStyledItemDelegate
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

import sys

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Создание профиля')
        self.setGeometry(300, 300, 400, 150) # Размеры окна
        self.init_ui()

    def init_ui(self):
        self.start_button = QPushButton('Старт')
        self.stop_button = QPushButton('Стоп')

        self.selecting = QComboBox()
        self.selecting.addItems(["Секундомер", "Отсчет вниз"])
        self.selecting.currentTextChanged.connect(self.on_selection_change)

        self.time_text = QLabel()
        self.time = "00:00"
        self.time_text.setText(f"Время: {self.time}")
        
        self.label = QLabel("Напишите что-нибудь:")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.update_label)

        grid = QGridLayout()

        grid.addWidget(self.start_button, 0, 0)
        grid.addWidget(self.stop_button, 0, 1)

        grid.addWidget(self.selecting, 1, 0, 1, 2)

        grid.addWidget(self.time_text, 2, 0)
        grid.addWidget(self.label, 3, 0)
        grid.addWidget(self.line_edit, 4, 0, 1, 2)
        self.setLayout(grid)

    def on_selection_change(self, text):
        if text == "Секундомер":
                self.time_text.setText(f"Время: 00:00")
        else:
                self.time_text.setText(f"Время: 59:59")

    def update_label(self, text):
         self.label.setText(f"Вы ввели: {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Timer()
    window.show()
    sys.exit(app.exec_())