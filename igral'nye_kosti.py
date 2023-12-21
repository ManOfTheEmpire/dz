import sys
import typing
import random
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication,QListWidget , QMainWindow , QLabel,  QVBoxLayout, QGridLayout, QWidget, QLineEdit, QPushButton, QMessageBox
 

class Window(QMainWindow):
    def __init__(self) :
        super(Window,self).__init__()
        self.centralwidget = QWidget(self) # Само окно
        self.setGeometry(250,150,350,400)


        self.knp = QPushButton(self) # кнопа броска кубиков
        self.knp.setText("Бросить кубики")
     
        self.brs = QLineEdit(self) # Поля для заполнения и ответ
        self.brs.setText("Количество бросков")
        self.brs.move(0,40)
        self.brs.adjustSize()
        self.chs = QLineEdit(self)
        self.chs.setText("Число кубиков")
        self.chs.move(0,80)
        self.chs.adjustSize()
        self.it = QListWidget(self)
        self.it.addItems(["Ответ:"])
        self.it.move(0,120)
        self.knp.clicked.connect(self.prow)
        self.it.adjustSize()
    

    def prow(self):
        self.it.clear()
        self.it.addItems(["Ответ:"])
        self.brs = int(self.brs.text())
        self.kl = int(self.chs.text())
        print(self.brs,self.kl)  
        self.results = []
        for i in range(self.brs):
             summa = 0
             for i in range(self.kl):
                x = random.randint(1, 6)
                summa += x
             self.results.append(summa)
        r = 0
        answ = ""
        for n in range(6*(self.kl)):
            r += 1
            a = self.results.count(r)
            print(r, '=', float((a / self.brs) * 100) ,'%')
            answ = str(r) + '=' + str(float((a / len(self.results)) * 100)) +'%' 
            self.it.addItem(str(answ))
 

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
if __name__ == "__main__":
    applic()