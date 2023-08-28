from typing import Optional
import PySide2.QtCore
import PySide2.QtWidgets
from app import *
from cadastroProduto import *

class Estoque(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estoque Mercado")
        self.setFixedSize(600,500)
        lbl_prod_cadastrados = QLabel("Produtos em Estoque: ")


    def produtos_em_estoque():
        
        list
        
app_estoque = QApplication(sys.argv)
w_estoque= Estoque()
w_estoque.show()
app_estoque.exec_()