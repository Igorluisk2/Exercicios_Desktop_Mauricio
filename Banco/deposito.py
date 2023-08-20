from app import *

#Função de depósito

def deposito(self):


        self.deposito_saldo = float(self.inp_deposito_inicial.text())
        self.saldo = self.saldo + self.deposito_saldo
        self.text_cadastro.append(f"\nDeposito Feito!\nNome do Titular: {self.nome}\nNúmero da Conta: {self.conta}\nSaldo: R${self.saldo}\n")