from typing import Optional
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication,QWidget,QLabel,QDialog,QPushButton,QVBoxLayout
import sys

class Estoque(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estoque Mercado")
        self.setFixedSize(600,500)
        #Labels
        lbl_prod_cadastrados = QLabel("Produtos em Estoque: ")
        
        
        #Layout Do Estoque 
        layout_estoque = QVBoxLayout(self)
        
        #Adicionando a Label ao Layout
        layout_estoque.addWidget(lbl_prod_cadastrados)
        


    def produtos_em_estoque():
        print('algumacoisa')
        
app_estoque = QApplication(sys.argv)
w_estoque= Estoque()
w_estoque.show()
app_estoque.exec_()