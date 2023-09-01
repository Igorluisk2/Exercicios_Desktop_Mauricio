import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
class CriarConta:
    def __init__(self, conta_app, numero_conta, titular_conta):
        self.conta_app = conta_app
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta

    def executar(self):
        self.conta_app.criar_conta(self.numero_conta, self.titular_conta)
