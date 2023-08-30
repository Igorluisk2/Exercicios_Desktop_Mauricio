import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class RealizarDeposito:
    def __init__(self, conta_app, valor):
        self.conta_app = conta_app
        self.valor = valor

    def executar(self):
        if self.conta_app.conta:
            self.conta_app.realizar_deposito(self.valor)
