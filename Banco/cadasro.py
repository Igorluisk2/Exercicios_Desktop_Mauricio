from app import *

#Função de cadastro

def cadastro(self):


    self.saldo = float(self.inp_deposito_inicial.text())
    self.nome = self.inp_nome.text()
    self.conta = int(self.inp_numero_conta.text())
    self.text_cadastro.append(f"\nNome do Titular: {self.nome}\nNúmero da Conta: {self.conta}\nSaldo: R${self.saldo}\nCadastro Feito com sucesso!\n")