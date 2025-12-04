from abc import ABC, abstractmethod
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
)
class LineEditCreator(ABC):
    @abstractmethod
    def create(self):
        pass
class HighlightLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Поле ")
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid gray;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid green;
                background-color: #eaffea;
            }
        """)
class PasswordLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Пароль")
        self.setEchoMode(QLineEdit.Password)
class FramedLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Поле с рамкой")
        self.setStyleSheet("border: 2px solid black; padding: 5px;")
class HighlightCreator(LineEditCreator):
    def create(self):
        return HighlightLineEdit()
class PasswordCreator(LineEditCreator):
    def create(self):
        return PasswordLineEdit()
class FramedCreator(LineEditCreator):
    def create(self):
        return FramedLineEdit()
class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация + Фабричный метод")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.combo = QComboBox()
        self.combo.addItems(["Highlight", "Password", "Framed"])
        self.combo.currentIndexChanged.connect(self.update_fields)
        layout.addWidget(self.combo)
        self.creator = HighlightCreator()
        self.login_field = self.creator.create()
        self.password_field = self.creator.create()
        layout.addWidget(self.login_field)
        layout.addWidget(self.password_field)
        btns = QHBoxLayout()
        self.btn_login = QPushButton("Войти")
        self.btn_register = QPushButton("Регистрация")
        btns.addWidget(self.btn_login)
        btns.addWidget(self.btn_register)
        layout.addLayout(btns)
        self.label = QLabel("Введите логин и пароль.")
        layout.addWidget(self.label)
        self.btn_login.clicked.connect(self.login_clicked)
        self.btn_register.clicked.connect(self.register_clicked)
    def update_fields(self):
        """Пересоздание полей через фабрику."""
        sel = self.combo.currentText()
        if sel == "Highlight":
            self.creator = HighlightCreator()
        elif sel == "Password":
            self.creator = PasswordCreator()
        else:
            self.creator = FramedCreator()
        self.login_field.deleteLater()
        self.password_field.deleteLater()
        self.login_field = self.creator.create()
        self.password_field = self.creator.create()
        self.layout().insertWidget(1, self.login_field)
        self.layout().insertWidget(2, self.password_field)
    def login_clicked(self):
        login = self.login_field.text()
        password = self.password_field.text()
        if not login or not password:
            self.label.setText("Ошибка: поля не могут быть пустыми.")
            return
        if login == "admin" and password == "1234":
            self.label.setText("Успешный вход!")
        else:
            self.label.setText("Неверный логин или пароль.")
    def register_clicked(self):
        login = self.login_field.text()
        password = self.password_field.text()
        if not login or not password:
            self.label.setText("Ошибка: поля пустые.")
            return

        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(f"{login}:{password}\n")

        self.label.setText("Пользователь зарегистрирован!")

if __name__ == "__main__":
    app = QApplication([])
    window = AuthWindow()
    window.resize(350, 250)
    window.show()
    app.exec()
