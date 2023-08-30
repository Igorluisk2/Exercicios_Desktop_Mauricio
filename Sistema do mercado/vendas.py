import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget

class VendasTab(QWidget):
    def __init__(self, mercado_app):
        super().__init__()
        self.mercado_app = mercado_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lista_vendas = QListWidget()
        layout.addWidget(self.lista_vendas)

        self.combo_produto = QComboBox()
        self.combo_produto.currentIndexChanged.connect(self.atualizar_rotulo_preco)
        layout.addWidget(QLabel("Selecione um Produto:"))
        layout.addWidget(self.combo_produto)

        self.rotulo_preco = QLabel()  # Rótulo de preço para o produto selecionado
        layout.addWidget(self.rotulo_preco)

        self.entrada_quantidade_vendas = QLineEdit()
        layout.addWidget(QLabel("Quantidade Vendida:"))
        layout.addWidget(self.entrada_quantidade_vendas)

        botao_adicionar_ao_carrinho = QPushButton("Adicionar ao Carrinho")
        botao_adicionar_ao_carrinho.clicked.connect(self.adicionar_ao_carrinho)
        layout.addWidget(botao_adicionar_ao_carrinho)

        self.lista_carrinho = QListWidget()
        layout.addWidget(self.lista_carrinho)

        self.rotulo_total = QLabel("Total: R$ 0.00")
        layout.addWidget(self.rotulo_total)

        botao_finalizar_venda = QPushButton("Finalizar Venda")
        botao_finalizar_venda.clicked.connect(self.mercado_app.vender_produtos)
        layout.addWidget(botao_finalizar_venda)

        self.setLayout(layout)

    def atualizar_combo_produto(self):
        self.combo_produto.clear()
        for produto in self.mercado_app.produtos:
            self.combo_produto.addItem(produto.nome)

    def atualizar_rotulo_preco(self, index):
        if index >= 0 and index < len(self.mercado_app.produtos):
            produto = self.mercado_app.produtos[index]
            self.rotulo_preco.setText(f"Preço: R$ {produto.preco:.2f}")

    def adicionar_ao_carrinho(self):
        indice_produto = self.combo_produto.currentIndex()
        produto = self.mercado_app.produtos[indice_produto]
        quantidade = int(self.entrada_quantidade_vendas.text())

        if quantidade > produto.quantidade:
            self.lista_vendas.addItem("Quantidade insuficiente em estoque.")
            return

        self.mercado_app.carrinho.append((produto, quantidade))
        self.atualizar_lista_carrinho()
        self.atualizar_rotulo_total()

        self.limpar_campos()

    def atualizar_lista_carrinho(self):
        self.lista_carrinho.clear()
        for produto, quantidade in self.mercado_app.carrinho:
            self.lista_carrinho.addItem(f"{produto.nome} - Quantidade: {quantidade}")

    def atualizar_rotulo_total(self):
        total_preco = sum(produto.preco * quantidade for produto, quantidade in self.mercado_app.carrinho)
        self.rotulo_total.setText(f"Total: R$ {total_preco:.2f}")

    def limpar_campos(self):
        self.entrada_quantidade_vendas.clear()
