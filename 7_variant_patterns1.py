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
        self.subsribers = []

    def subscibe(self, callback):
        self.subsribers.append(callback)

    def notify(self):
        for callback in self.subsribers:
            callback(self.value)

    def increment(self):
        self.value += 1
        self.notify()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Наблюдатель")
        self.setGeometry(300, 300, 400, 150)
        self.total = 0
        self.init_ui()

    def init_ui(self):
        self.plus_one_button = QPushButton()
        self.plus_one_button.setText("+1")
        self.plus_one_button.clicked.connect(self.update_subsribers)

        self.subsribers_count = QLabel()
        self.subsribers_count.setText(f"Количество подписчиков: 0")

        grid = QGridLayout()

        grid.addWidget(self.plus_one_button, 0, 0, 1, 2)
        grid.addWidget(self.subsribers_count, 1, 0, 1, 2)

        self.setLayout(grid)

        self.counter_model = CounterModel()
        self.counter_model.__init__()


    def update_subsribers(self):
        self.total = self.total + 1
        self.subsribers_count.setText(f"Количество подписчиков: {self.total}")
        # self.counter_model.subscibe(self.counter_model.value)
        # self.counter_model.increment()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())