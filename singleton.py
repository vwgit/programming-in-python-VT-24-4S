import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QVBoxLayout, QComboBox, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QFont

class SettingsManager(QObject):
    theme = "light"
    font_size = 10
    language = "ru"
    settings_changed = pyqtSignal()
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        super().__init__()
        if not hasattr(self, "initialized"):
            self.theme = "light"
            self.font_size = 14
            self.language = "en"
            self.initialized = True
    def update_settings(self, theme = None, font_size = None, language = None):
        if theme is not None:
            self.theme = theme
        if font_size is not None:
            self.font_size = font_size
        if language is not None:
            self.language = language
        
        self.settings_changed.emit()


class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = SettingsManager()
        layout = QVBoxLayout()
        self.theme_box = QComboBox()
        self.theme_box.addItems(["light", "dark"])
        layout.addWidget(QLabel("Выберите тему: "))
        layout.addWidget(self.theme_box)
        self.font_size_box = QComboBox()
        self.font_size_box.addItems(["14", "16", "18"])
        layout.addWidget(QLabel("Выберите шрифт: "))
        layout.addWidget(self.font_size_box)
        self.language_box = QComboBox()
        self.language_box.addItems(["en", "ru", "kz"])
        layout.addWidget(QLabel("Выберите язык: "))
        layout.addWidget(self.language_box)

        self.setLayout(layout)
        self.theme_box.currentTextChanged.connect(self.apply_settings)
        self.font_size_box.currentTextChanged.connect(self.apply_settings)
        self.language_box.currentTextChanged.connect(self.apply_settings)


    def apply_settings(self):
        self.manager.update_settings(
            theme = self.theme_box.currentText(),
            font_size = self.font_size_box.currentText(),
            language = self.language_box.currentText()
        )

class PreviewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = SettingsManager()
        layout = QVBoxLayout()
        self.label = QLabel("Text")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.manager.settings_changed.connect(self.update_view)
        self.update_view()

    def update_view(self):
        print("Text1")
        font = QFont()
        font.setPointSize(int(self.manager.font_size))
        self.label.setFont(font)
        if self.manager.language == "en":
            text = "Hello world"
        elif self.manager.language == "ru":
            text = "Привет мир"
        elif self.manager.language == "kz":
            text = "Салем алем"

        self.label.setText(text)

        if self.manager.theme == "light":
            self.setStyleSheet("""
background-color: white;
color: black;
""")
        elif self.manager.theme == "dark":
            self.setStyleSheet("""
background-color: dark;
color: white;
""")

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
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())