import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
from cadastrar import CadastroTab,Produto
from estoque import EstoqueTab
from vendas import VendasTab

class MercadoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.produtos = []
        self.carrinho = []

        self.setWindowTitle("Mercadinho Do Senac")
        self.setGeometry(100, 100, 800, 600)

        self.abas = QTabWidget()
        self.aba_cadastro = CadastroTab(self)
        self.aba_estoque = EstoqueTab(self)
        self.aba_vendas = VendasTab(self)

        self.abas.addTab(self.aba_cadastro, "Cadastro")
        self.abas.addTab(self.aba_estoque, "Estoque")
        self.abas.addTab(self.aba_vendas, "Vendas")

        self.iniciar_interface()

    def iniciar_interface(self):
        layout = QVBoxLayout()
        layout.addWidget(self.abas)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def cadastrar_produto(self):
        nome = self.aba_cadastro.entrada_nome.text()
        preco = float(self.aba_cadastro.entrada_preco.text())
        quantidade = int(self.aba_cadastro.entrada_quantidade.text())

        produto = Produto(nome, preco, quantidade)
        self.produtos.append(produto)

        self.aba_estoque.atualizar_lista_estoque()
        self.aba_vendas.atualizar_combo_produto()
        self.aba_vendas.atualizar_rotulo_preco(self.aba_vendas.combo_produto.currentIndex())
        self.aba_cadastro.limpar_campos()

        self.aba_cadastro.rotulo_mensagem_cadastro.setText("Produto cadastrado com sucesso!")

    def vender_produtos(self):
        total_preco = 0.0
        for produto, quantidade in self.carrinho:
            if quantidade > produto.quantidade:
                self.aba_vendas.lista_vendas.addItem(f"Quantidade insuficiente para {produto.nome}.")
                return

            produto.quantidade -= quantidade
            total_preco += produto.preco * quantidade

        self.carrinho = []
        self.aba_vendas.atualizar_lista_carrinho()
        self.aba_estoque.atualizar_lista_estoque()
        self.aba_vendas.atualizar_rotulo_total()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mercado_app = MercadoApp()
    mercado_app.show()
    sys.exit(app.exec_())