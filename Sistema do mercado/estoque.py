from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from app import *
from cadastroProduto import Cadastro

class Estoque(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estoque Mercado")
        self.setFixedSize(600,500)
        lbl_prod_cadastrados = QLabel("Produtos em Estoque: ")


    def produtos_em_estoque():
        
        list
        
app = QApplication(sys.argv)
w = Estoque()
w.show()
app.exec()