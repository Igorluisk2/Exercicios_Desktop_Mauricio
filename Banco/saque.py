import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
class RealizarSaque:
    def __init__(self, conta_app, valor):
        self.conta_app = conta_app
        self.valor = valor

    def executar(self):
        if self.conta_app.conta:
            if self.conta_app.realizar_saque(self.valor):
                return "Saque realizado com sucesso."
            else:
                return "Saldo insuficiente."
        return None