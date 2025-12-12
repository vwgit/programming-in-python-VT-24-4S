from PyQt5.QtWidgets import (
     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
     QLabel, QPushButton, QLineEdit, QComboBox, QGridLayout, QStyledItemDelegate
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

import sys

class CounterModel():
    def __init__(self):
        self.value = 0
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self):
        for callback in self.subscribers:
            callback(self.value)

    def increment(self):
        self.value += 1
        self.notify()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Наблюдатель")
        self.setGeometry(300, 300, 400, 150)
        self.init_ui()
        self.counter_model.subscribe(self.update_label)

    def init_ui(self):
        self.plus_one_button = QPushButton()
        self.plus_one_button.setText("+1")
        self.counter_model = CounterModel()
        self.plus_one_button.clicked.connect(self.counter_model.increment)

        self.subscribers_label = QLabel("Количество: 0")

        grid = QGridLayout()

        grid.addWidget(self.plus_one_button, 0, 0, 1, 2)
        grid.addWidget(self.subscribers_label, 1, 0, 1, 2)

        self.setLayout(grid)


    def update_label(self, value):
        self.subscribers_label.setText(f"Количество: {value}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())