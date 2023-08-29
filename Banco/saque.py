from app import *
#Função de Saque
def sacar(self):
    self.retirar=int(self.totaldep.text())-int(self.sacar_Qline.text())-5
    self.retirarstr=str(self.retirar)
        
    if self.retirar>=0:
        self.sacar_Qlabel.setText('Saldo  = R$ {},00'.format(self.retirar))
        self.totaldep.setText(self.retirarstr)
    else:
        self.sacar_Qlabel.setText('Saldo insuficiente!!\nFavor entrar em contato com seu gerente para uma possível liberação de limite de conta')