from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QLayout,QLineEdit,QHBoxLayout,QVBoxLayout,QWidget,QTextBrowser
import sys
class Banco(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vulgo-Senacoin")
        self.layout = QVBoxLayout()


        #Cadastro Cliente
        self.lbl_nome = QLabel("Nome:")
        self.lbl_numero_conta = QLabel("Número da Conta:")
        self.lbl_deposito_inicial = QLabel("Deposito Inicial:")
        
        self.inp_nome = QLineEdit(self)
        self.inp_numero_conta = QLineEdit(self)
        self.inp_deposito_inicial = QLineEdit(self)
        self.text_cadastro = QTextBrowser(self)

        #Botão
        self.btn_cadastro = QPushButton("Cadastrar")
        self.btn_deposito = QPushButton("Depositar")
        self.btn_sacar = QPushButton("Sacar")
        self.btn_cadastro.clicked.connect(self.cadastro)
        self.btn_deposito.clicked.connect(self.deposito)
        self.btn_sacar.clicked.connect(self.saque)
        
        
        
        #Colocando as labels como 
        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.inp_nome)
        self.layout.addWidget(self.lbl_numero_conta)
        self.layout.addWidget(self.inp_numero_conta)
        self.layout.addWidget(self.lbl_deposito_inicial)
        self.layout.addWidget(self.inp_deposito_inicial)
        self.layout.addWidget(self.btn_cadastro)
        self.layout.addWidget(self.btn_deposito)
        self.layout.addWidget(self.btn_sacar)
        self.layout.addWidget(self.text_cadastro)
        self.setLayout(self.layout)

    def cadastro(self):
        self.saldo = float(self.inp_deposito_inicial.text())
        self.nome = self.inp_nome.text()
        self.conta = int(self.inp_numero_conta.text())

        self.text_cadastro.append(f"\nNome do Titular: {self.nome}\nNúmero da Conta: {self.conta}\nSaldo: R${self.saldo}\nCadastro Feito com sucesso!\n")

    def deposito(self):
        self.deposito_saldo = float(self.inp_deposito_inicial.text())
        self.saldo = self.saldo + self.deposito_saldo
        self.text_cadastro.append(f"\nDeposito Feito!\nNome do Titular: {self.nome}\nNúmero da Conta: {self.conta}\nSaldo: R${self.saldo}\n")

    def saque(self):
        #Arrrumar o saque !!!!!
        self.deposito_saldo = float(self.inp_deposito_inicial.text())
        self.saldo =  (self.deposito_saldo + 5) 
        if self.saldo < 0:
            self.text_cadastro.append(f"\nSaldo insuficente para saque!\n")
        else:
            self.text_cadastro.append(f"\nVocê Sacou!\nNome do Titular: {self.nome}\nNúmero da Conta: {self.conta}\nSaldo: R${self.saldo}\n")

appl = QApplication(sys.argv)
window = Banco() 
window.show()
appl.exec()
