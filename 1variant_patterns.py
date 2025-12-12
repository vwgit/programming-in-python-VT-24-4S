import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QRadioButton
)

# =========================
# 1. БАЗОВАЯ КНОПКА
# =========================
class BaseButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)


# =========================
# 2. КОНКРЕТНЫЕ КНОПКИ
# =========================
class DefaultButton(BaseButton):
    def __init__(self):
        super().__init__("Обычная кнопка")


class SuccessButton(BaseButton):
    def __init__(self):
        super().__init__("Ты хороший человек!")
        self.setStyleSheet("background-color: green; color: white;")


class DangerButton(BaseButton):
    def __init__(self):
        super().__init__("Ты серьёзно решил нажать эту кнопку? НЕ ДЕЛАЙ ЭТОГО!!!")
        self.setStyleSheet("background-color: red; color: white;")


# =========================
# 3. FACTORY
# =========================
class ButtonFactory:
    @staticmethod
    def create_button(button_type):
        if button_type == "success":
            return SuccessButton()
        elif button_type == "danger":
            return DangerButton()
        else:
            return DefaultButton()


# =========================
# 4. ГЛАВНОЕ ОКНО
# =========================
class FactoryDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bimba")
        self.resize(300, 200)

        # Сохраняем ссылку на layout, чтобы обращаться к нему позже
        self.main_layout = QVBoxLayout()

        # --- Radio buttons ---
        self.rb_default = QRadioButton("Обычная кнопка")
        self.rb_success = QRadioButton("Нажми сюда!")
        self.rb_danger = QRadioButton("Bimba")

        self.rb_default.setChecked(True)

        self.main_layout.addWidget(self.rb_default)
        self.main_layout.addWidget(self.rb_success)
        self.main_layout.addWidget(self.rb_danger)

        # --- Кнопка, созданная через Factory ---
        self.button = ButtonFactory.create_button("default")
        self.main_layout.addWidget(self.button)

        # --- Сигналы ---
        self.rb_default.toggled.connect(self.update_button)
        self.rb_success.toggled.connect(self.update_button)
        self.rb_danger.toggled.connect(self.update_button)

        self.setLayout(self.main_layout)

    def update_button(self):
        # Проверяем отправителя, чтобы избежать лишних перерисовок (toggled срабатывает дважды: для выкл и вкл)
        sender = self.sender()
        if not sender.isChecked():
            return

        # Удаляем старую кнопку из layout и памяти
        self.main_layout.removeWidget(self.button)
        self.button.deleteLater()

        # Определяем тип
        if self.rb_success.isChecked():
            btn_type = "success"
        elif self.rb_danger.isChecked():
            btn_type = "danger"
        else:
            btn_type = "default"

        # Создаём новую кнопку через Factory
        self.button = ButtonFactory.create_button(btn_type)
        self.main_layout.addWidget(self.button)


# =========================
# 5. ЗАПУСК
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FactoryDemo()
    window.show()
    sys.exit(app.exec_())
