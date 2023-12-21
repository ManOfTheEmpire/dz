import random
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Угадайте число')
        self.setGeometry(150, 150, 350, 250)

        self.random_chis = random.randint(1, 100)
        self.chis = 10

        layout = QVBoxLayout()

        self.label = QLabel('Введите число от 1 до 100:')
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.button = QPushButton('Попробовать')
        self.button.clicked.connect(self.guess_number)
        layout.addWidget(self.button)

        self.result = QLabel('')
        layout.addWidget(self.result)

        self.setLayout(layout)

    def guess_number(self):
        pop = int(self.input.text())
        if pop < self.random_chis:
            self.result.setText('Загаданное число больше')
        if pop > self.random_chis:
            self.result.setText('Загаданное число меньше')
        if pop == self.random_chis:
            self.result.setText('Вы угадали')
        self.chis -= 1
        if self.chis == 0:
            self.result.setText('Вы проиграли. Было загадано число: ' + str(self.random_chis))
            self.button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())