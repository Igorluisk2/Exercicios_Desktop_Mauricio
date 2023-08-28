#Mercado
import typing
import sys
from typing import Optional
from PySide2.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget,QPushButton,QTextBrowser
from PySide2.QtCore import Qt


class Mercado(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mercado Senac")
        self.setFixedSize(600,500)


app = QApplication(sys.argv)
w = Mercado()
w.show()
app.exec()