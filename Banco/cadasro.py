from app import *

#Função de cadastro
def cadastrar_conta(self):
    self.registrarConta.setText('Conta Aberta com sucesso!!!\nAgência = {}\nConta = {}\nSaldo = R$ {},00'
        .format(self.agencia.text(), self.conta.text(), self.totaldep.text()))
    self.abrirContaButton.deleteLater()