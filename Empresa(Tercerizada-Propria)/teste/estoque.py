import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget


class EstoqueTab(QWidget):
    def __init__(self, mercado_app):
        super().__init__()
        self.mercado_app = mercado_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lista_estoque = QListWidget()
        layout.addWidget(self.lista_estoque)

        self.setLayout(layout)

    def atualizar_lista_estoque(self):
        self.lista_estoque.clear()
        for funcio in self.mercado_app.funcionarios:
            self.lista_estoque.addItem(f"{funcio.nome} - Pagamento = {funcio.vhora*horast}")