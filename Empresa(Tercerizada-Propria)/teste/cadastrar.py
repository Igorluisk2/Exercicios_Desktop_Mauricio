import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget

class funcio:
    def __init__(self, nome, horast, vhora):
        self.nome = nome
        self.horast = horast
        self.vhora = vhora

class CadastroTab(QWidget):
    def __init__(self, mercado_app):
        super().__init__()
        self.mercado_app = mercado_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.entrada_nome = QLineEdit()
        self.entrada_horast = QLineEdit()
        self.entrada_vhora = QLineEdit()

        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.clicked.connect(self.mercado_app.cadastrar_funcio)

        layout.addWidget(QLabel("Nome do Funcionário:"))
        layout.addWidget(self.entrada_nome)
        layout.addWidget(QLabel("Horas trabalhadas:"))
        layout.addWidget(self.entrada_horast)
        layout.addWidget(QLabel("Valor da hora:"))
        layout.addWidget(self.entrada_vhora)
        layout.addWidget(botao_cadastrar)

        self.rotulo_mensagem_cadastro = QLabel()
        layout.addWidget(self.rotulo_mensagem_cadastro)

        self.setLayout(layout)

    def limpar_campos(self):
        self.entrada_nome.clear()
        self.entrada_horast.clear()
        self.entrada_vhora.clear()