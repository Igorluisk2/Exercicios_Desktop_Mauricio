import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class ContaBancaria:
    def __init__(self, numero_conta, titular_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor + 5:
            self.saldo -= valor + 5
            return True
        else:
            return False
    
    def obter_saldo(self):
        return self.saldo
    
class ContaBancariaApp:
    def __init__(self):
        self.conta = None

    def criar_conta(self, numero_conta, titular_conta):
        self.conta = ContaBancaria(numero_conta, titular_conta)

    def realizar_deposito(self, valor):
        if self.conta:
            self.conta.depositar(valor)

    def realizar_saque(self, valor):
        if self.conta:
            return self.conta.sacar(valor)

    def obter_saldo(self):
        if self.conta:
            return self.conta.obter_saldo()
        else:
            return None