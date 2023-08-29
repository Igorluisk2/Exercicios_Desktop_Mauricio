from app import *

#Função de depósito

def depositar(self):
        self.saldo=int(self.valor_Qline.text())+int(self.totaldep.text())
        self.saldostr=str(self.saldo)
        self.valor_Qlabel.setText('Saldo = R$ {},00'.format(self.saldo))
        self.totaldep.setText(self.saldostr)