from PySide2.QtCore import QSize
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,QCheckBox,QFormLayout,QWidget

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##titulo da janela##
        self.setWindowTitle('Seu Banco')
        self.setFixedSize(QSize(700,500))
        
        ##linhas para digitar a agencia e conta##
        self.agencia=QLineEdit(self)
        self.conta=QLineEdit(self)
        
        ##label para perguntar se deseja deposito inicial##
        self.pergunta=QLabel('Deseja fazer deposito inicial?')
    
        ##chekbox para responder a pergunta do deposito inicial##
        self.depositoS=QCheckBox('Sim')
        self.depositoN=QCheckBox('Não')
        self.depositoS.stateChanged.connect(self.state)
        self.depositoN.stateChanged.connect(self.state2)
        
        ##linha para digitar o valor do dep inicial##
        self.valorDepInicial_Qline=QLineEdit(self)
        self.totaldep=self.valorDepInicial_Qline
        
        
        
        ##label para mostrar o valor digitado 
        self.valorDepInicial_Qlabel=QLabel()
        
        
        #botão para abrir a conta#
        self.abrirContaButton=QPushButton('Abrir conta',self)
        self.abrirContaButton.clicked.connect(self.cadastrar_conta)
        
        #espaço que mostra os dados da conta
        self.registrarConta=QLabel(self)
        
        #botao para depositar
        self.depButton=QPushButton('Depositar',self)
        self.depButton.clicked.connect(self.depositar)
        
        #linha para digitar o valor dep apos abertura da conta
        self.valor_Qline=QLineEdit(self)
        
        #label para mostrar o resultado do dep apos abertura da conta
        self.valor_Qlabel=QLabel(self)
        
        #botao sacar
        self.sacar_QButon=QPushButton('Sacar',self)
        self.sacar_QButon.clicked.connect(self.sacar)
        
        #linha para sacar
        self.sacar_Qline=QLineEdit(self)
        
        #label para mostrar o resultado do saque
        self.sacar_Qlabel=QLabel()
        
        ##formatação dos Widgets##
        pagina=QFormLayout(self)
        pagina.addRow('Agência = ',self.agencia)
        pagina.addRow('Conta = ',self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('valor que deseja depositar\saldo = ',self.totaldep)
        pagina.addRow(self.abrirContaButton)
        pagina.addRow(self.registrarConta)
        pagina.addRow('Valor do deposito = ',self.valor_Qline)
        pagina.addRow(self.depButton)
        pagina.addRow(self.valor_Qlabel)
        pagina.addRow('valor do saque(ATENÇÃO!! cobrança de R$ 5,00 por saque) = ',self.sacar_Qline)
        pagina.addRow(self.sacar_QButon)
        pagina.addRow(self.sacar_Qlabel)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
        
    def state(self,s):#se tiver dep inicial#
        if s == 2:
            self.depositoN.deleteLater() 
            self.totaldep.text()
            
            
    def state2(self, s):#se não tiver dep inicial#
        if s == 2:
            self.depositoS.deleteLater()
            self.totaldep.setText('0')
            
    def cadastrar_conta(self):
        self.registrarConta.setText('Conta Aberta com sucesso!!!\nAgência = {}\nConta = {}\nSaldo = R$ {},00'
        .format(self.agencia.text(), self.conta.text(), self.totaldep.text()))
        self.abrirContaButton.deleteLater()
        
        
    def depositar(self):
        self.saldo=int(self.valor_Qline.text())+int(self.totaldep.text())
        self.saldostr=str(self.saldo)
        self.valor_Qlabel.setText('Saldo = R$ {},00'.format(self.saldo))
        self.totaldep.setText(self.saldostr)
        
    def sacar(self):
        self.retirar=int(self.totaldep.text())-int(self.sacar_Qline.text())-5
        self.retirarstr=str(self.retirar)
        
        if self.retirar>=0:
            self.sacar_Qlabel.setText('Saldo  = R$ {},00'.format(self.retirar))
            self.totaldep.setText(self.retirarstr)
        else:
            self.sacar_Qlabel.setText('Saldo insuficiente!!\nFavor entrar em contato com seu gerente para uma possível liberação de limite de conta')
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec_()