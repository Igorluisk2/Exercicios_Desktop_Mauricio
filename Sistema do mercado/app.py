#Mercado
import typing
import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget
from PySide2.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Mercado Senac")
        #Ajustando o Layou da janela
        self.layout = QVBoxLayout(self)
        
        #Labels
        #Cadastrar os produtos do mercado
        self.lbl_mercado = QLabel("Bem Vindos ao Mercado do Senac!")
        self.lbl_prod_nome = QLabel("Nome do Produto: ")#Label Nome do Produto
        self.lbl_prod_preco = QLabel("Preço do Produto: ")#Label Preço do Produto
        self.lbl_prod_unid = QLabel("Quantidade de Produto: ")#Label de Quantidades do Produto
        
        #LineEdits
        self.inp_prod_nome = QLineEdit(self)#Input Nome do Produto
        self.inp_prod_preco = QLineEdit(self)#Input Preço do Produto
        self.inp_prod_unid = QLineEdit(self)#Input de Quantidade do Produto
        
        #Sets de Layout na janela do programa
        self.layout.addWidget(self.lbl_mercado)
        self.layout.addWidget(self.lbl_prod_nome)
        self.layout.addWidget(self.inp_prod_nome)
        self.layout.addWidget(self.lbl_prod_preco)
        self.layout.addWidget(self.inp_prod_preco)
        self.layout.addWidget(self.lbl_prod_unid)
        self.layout.addWidget(self.inp_prod_unid)
        
        
         
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()