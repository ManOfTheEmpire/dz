
import random
import sys
import typing
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication ,QListWidget , QMainWindow , QLabel,  QVBoxLayout, QGridLayout, QWidget, QLineEdit, QPushButton, QMessageBox

f = open("periodictable.csv")
tabl = f.read()
tabl = tabl.splitlines()
class Window(QMainWindow):
    def __init__(self) :
        super(Window,self).__init__()
        self.centralwidget =QWidget(self)
        self.setGeometry(500,300,700,750)

        self.bat = QPushButton(self)
        
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 700,500))
        self.pixmap = QPixmap("1920dd04dccc296ae63644e4845af50b.jpg")
        self.label.setPixmap(self.pixmap)
        
        self.rull = QLineEdit(self)
        self.rull.move(250,500)

        self.bat.setText("Информация")
        self.bat.clicked.connect(self.prow)
        self.answ = QLabel(self)
        self.enter= self.rull.text()
        self.bat.move(150,500)
        self.answ.setGeometry(QtCore.QRect(0, 500, 210, 210))
    def prow(self):
        self.enter= self.rull.text()
        for k in tabl:
            if k.split(",")[1] == self.enter:
                 k=k.split(",")
                 self.answ.setText(f"Номер:{k[0]}\n Символ:{k[1]}\n Элемент:{k[2]}\n Латинское название:{k[3]}\n Группа:{k[4]}\n Период:{k[5]}\n Атомная масса:{k[6]}  u\n Плотность:{k[7]}  g/cm*3\n Температура плавления:{k[8]} K\n Температура кипения:{k[9]} K\n Удельная теплоёмкость:{k[10]}  J/(g*k)\n Электроотрицательность:{k[11]}\n Содержание в земной коре:{k[12]}  мг/кг")
   

def applic():
        app = QApplication(sys.argv)
        window = Window()

        window.show()
        sys.exit(app.exec())
if __name__ == "__main__":
    applic()