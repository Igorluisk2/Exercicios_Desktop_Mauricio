import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class CadastroTab(QWidget):
    def __init__(self, mercado_app):
        super().__init__()
        self.mercado_app = mercado_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.entrada_nome = QLineEdit()
        self.entrada_preco = QLineEdit()
        self.entrada_quantidade = QLineEdit()

        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.clicked.connect(self.mercado_app.cadastrar_produto)

        layout.addWidget(QLabel("Nome do Produto:"))
        layout.addWidget(self.entrada_nome)
        layout.addWidget(QLabel("Preço Unitário:"))
        layout.addWidget(self.entrada_preco)
        layout.addWidget(QLabel("Quantidade em Estoque:"))
        layout.addWidget(self.entrada_quantidade)
        layout.addWidget(botao_cadastrar)

        self.rotulo_mensagem_cadastro = QLabel()
        layout.addWidget(self.rotulo_mensagem_cadastro)

        self.setLayout(layout)

    def limpar_campos(self):
        self.entrada_nome.clear()
        self.entrada_preco.clear()
        self.entrada_quantidade.clear()