import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from deposito import RealizarDeposito
from contabancaria import ContaBancaria,ContaBancariaApp
from cadastroconta import CriarConta
from saque import RealizarSaque

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicação Bancária")
        self.setGeometry(100, 100, 400, 300)

        self.conta_app = ContaBancariaApp()

        self.layout = QVBoxLayout()

        self.layout_campos = QVBoxLayout()

        self.label_numero_conta = QLabel("Número da Conta:")
        self.input_numero_conta = QLineEdit()

        self.label_titular_conta = QLabel("Titular da Conta:")
        self.input_titular_conta = QLineEdit()

        self.layout_campos.addWidget(self.label_numero_conta)
        self.layout_campos.addWidget(self.input_numero_conta)
        self.layout_campos.addWidget(self.label_titular_conta)
        self.layout_campos.addWidget(self.input_titular_conta)

        self.layout.addLayout(self.layout_campos)

        self.layout_botoes = QHBoxLayout()

        self.label_saldo = QLabel("Saldo:")
        self.label_saldo_display = QLabel("N/A")

        self.layout_botoes.addWidget(self.label_saldo)
        self.layout_botoes.addWidget(self.label_saldo_display)

        self.layout.addLayout(self.layout_botoes)

        self.botao_criar_conta = QPushButton("Criar Conta")
        self.botao_criar_conta.clicked.connect(self.criar_conta)

        self.botao_deposito = QPushButton("Depósito")
        self.botao_deposito.clicked.connect(self.deposito)

        self.botao_saque = QPushButton("Saque")
        self.botao_saque.clicked.connect(self.saque)

        self.layout.addWidget(self.botao_criar_conta)

        self.layout_botoes_op = QHBoxLayout()

        self.label_valor_deposito = QLabel("Valor do Depósito:")
        self.input_valor_deposito = QLineEdit()
        self.layout_botoes_op.addWidget(self.label_valor_deposito)
        self.layout_botoes_op.addWidget(self.input_valor_deposito)
        self.layout_botoes_op.addWidget(self.botao_deposito)

        self.label_valor_saque = QLabel("Valor do Saque:")
        self.input_valor_saque = QLineEdit()
        self.layout_botoes_op.addWidget(self.label_valor_saque)
        self.layout_botoes_op.addWidget(self.input_valor_saque)
        self.layout_botoes_op.addWidget(self.botao_saque)

        self.layout.addLayout(self.layout_botoes_op)

        self.label_mensagem = QLabel()
        self.layout.addWidget(self.label_mensagem)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def criar_conta(self):
        numero_conta = self.input_numero_conta.text()
        titular_conta = self.input_titular_conta.text()

        if numero_conta and titular_conta:
            CriarConta(self.conta_app, numero_conta, titular_conta).executar()
            self.atualizar_exibicao_saldo()

    def deposito(self):
        if self.conta_app.conta:
            valor_deposito = float(self.input_valor_deposito.text()) if self.input_valor_deposito.text() else 0
            RealizarDeposito(self.conta_app, valor_deposito).executar()
            self.atualizar_exibicao_saldo()

    def saque(self):
        if self.conta_app.conta:
            valor_saque = float(self.input_valor_saque.text()) if self.input_valor_saque.text() else 0
            mensagem = RealizarSaque(self.conta_app, valor_saque).executar()
            if mensagem is not None:
                self.label_mensagem.setText(mensagem)
            self.atualizar_exibicao_saldo()

    def atualizar_exibicao_saldo(self):
        saldo = self.conta_app.obter_saldo()
        if saldo is not None:
            self.label_saldo_display.setText(f"R$ {saldo:.2f}")
        else:
            self.label_saldo_display.setText("N/A")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = GUI()
    janela.show()
    sys.exit(app.exec())