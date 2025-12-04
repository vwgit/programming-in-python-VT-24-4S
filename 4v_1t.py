from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QVBoxLayout, QComboBox, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QFont

import sys
import io
import matplotlib as plt

class AppState:
    _instance = None

def __new__(cls):
    if cls._instance is None:
        cls._instance = super().__new__(cls)
        cls._instance.counter = 0
    return cls._instance

def inc(self):
    self.counter += 1

def get(self):
    return self.counter





class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.settings_widget = SettingsWidget()
        self.preview_widget = PreviewWidget()
        self.layout.addWidget(self.settings_widget)
        self.layout.addWidget(self.preview_widget)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        
        self.setWindowTitle('QCheckBox')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mywindow = QWidget()
    mywindow.resize(250, 150)

    mywindow.setWindowTitle('Singelton')
    mywindow.show()

    sys.exit(app.exec_())
    