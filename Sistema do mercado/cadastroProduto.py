#Mercado
import typing
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget,QPushButton,QTextBrowser
from PySide6.QtCore import Qt


class Cadastro(QWidget):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Mercado Senac")
        self.setFixedSize(600,500)
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
        
        #Botão 
        self.btn_cadastrar_produto = QPushButton("Cadastrar")
        self.btn_cadastrar_produto.clicked.connect(self.produto)
        
        #Layout de texto
        self.caixa_texto = QTextBrowser()
        
        
        #Sets de Layout na janela do programa
        self.layout.addWidget(self.lbl_mercado)
        self.layout.addWidget(self.lbl_prod_nome)
        self.layout.addWidget(self.inp_prod_nome)
        self.layout.addWidget(self.lbl_prod_preco)
        self.layout.addWidget(self.inp_prod_preco)
        self.layout.addWidget(self.lbl_prod_unid)
        
        self.layout.addWidget(self.inp_prod_unid)
        self.layout.addWidget(self.btn_cadastrar_produto)
        self.layout.addWidget(self.caixa_texto)
        
        
    def produto(self,preco=0,quantidade=0 ):
        nome = str(self.inp_prod_nome.text())
        quantidade = int(self.inp_prod_preco.text())
        preco = float(self.inp_prod_unid.text())
        self.caixa_texto.setText(f"Produto cadastrado com Sucesso!\nPreço: R${preco}\nQuantidade: {quantidade}")
        if quantidade == 0 or preco == 0 :
            self.caixa_texto.setText(f"Adicione valores a Preço e Quantidade!")
        
        else:
            list_nome_prod = []
            list_preco_prod = []
            list_quantidade_prod = []
            
            list_nome_prod.append(nome)
            list_preco_prod.append(preco)
            list_quantidade_prod.append(quantidade)
            self.caixa_texto.setText(f"Produto Cadastrado com sucesso!\nProduto: {nome}\nPreço: {preco}\nQuantidade: {quantidade}")
            
            
        
app = QApplication(sys.argv)
w = Cadastro()
w.show()
app.exec()