from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from cpf_window import CPFWindow
from cnpj_window import CNPJWindow
from PySide6.QtCore import (QSize)
from PySide6.QtGui import (QIcon,QPixmap)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('EXERCÍCIO 3 - CONTRIBUINTES')
        self.setFixedSize(QSize(350,250))
        
        self.cpf_window=QPushButton('CPF',self)
        self.cpf_window.setIcon(QIcon('cpf'))
        self.cpf_window.setGeometry(60,30,70,60)
        self.cpf_window.clicked.connect(self.open_cpf_window)
        
        self.cnpj_window=QPushButton('CNPJ',self)
        self.cnpj_window.setIcon(QIcon('cnpj'))
        self.cnpj_window.setGeometry(160,30,70,60)
        self.cnpj_window.clicked.connect(self.open_cnpj_window)

    def open_cpf_window(self):
        self.cpf_window = CPFWindow()
        self.cpf_window.show()
        

    def open_cnpj_window(self):
        self.cnpj_window = CNPJWindow()
        self.cnpj_window.show()
        
app=QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
    