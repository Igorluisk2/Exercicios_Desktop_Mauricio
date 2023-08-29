import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
class SalesTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        layout = QVBoxLayout()

        self.sales_list = QListWidget()
        layout.addWidget(self.sales_list)

        self.product_combobox = QComboBox()
        self.product_combobox.currentIndexChanged.connect(self.update_price_label)
        layout.addWidget(QLabel("Selecione um Produto:"))
        layout.addWidget(self.product_combobox)

        self.price_label = QLabel()  # Price label for selected product
        layout.addWidget(self.price_label)

        self.quantity_input_sales = QLineEdit()
        layout.addWidget(QLabel("Quantidade Vendida:"))
        layout.addWidget(self.quantity_input_sales)

        add_to_cart_button = QPushButton("Adicionar ao Carrinho")
        add_to_cart_button.clicked.connect(self.add_to_cart)
        layout.addWidget(add_to_cart_button)

        self.cart_list = QListWidget()
        layout.addWidget(self.cart_list)

        self.total_label = QLabel("Total: R$ 0.00")
        layout.addWidget(self.total_label)

        sell_button = QPushButton("Finalizar Venda")
        sell_button.clicked.connect(self.sell_products)
        layout.addWidget(sell_button)

        self.setLayout(layout)

    def update_product_combobox(self):
        self.product_combobox.clear()
        for product in self.parent.products:
            self.product_combobox.addItem(product.name)

    def update_price_label(self, index):
        if index >= 0 and index < len(self.parent.products):
            product = self.parent.products[index]
            self.price_label.setText(f"Preço: R$ {product.price:.2f}")

    def add_to_cart(self):
        product_index = self.product_combobox.currentIndex()
        product = self.parent.products[product_index]
        quantity = int(self.quantity_input_sales.text())

        if quantity > product.quantity:
            self.sales_list.addItem("Quantidade insuficiente em estoque.")
            return

        self.parent.cart.append((product, quantity))
        self.update_cart_list()
        self.update_total_label()

    def update_cart_list(self):
        self.cart_list.clear()
        for product, quantity in self.parent.cart:
            self.cart_list.addItem(f"{product.name} - Quantidade: {quantity}")

    def sell_products(self):
        total_price = 0.0
        for product, quantity in self.parent.cart:
            if quantity > product.quantity:
                self.sales_list.addItem(f"Quantidade insuficiente para {product.name}.")
                return

            product.quantity -= quantity
            total_price += product.price * quantity

        self.parent.cart = []
        self.update_cart_list()
        self.parent.tab_stock.update_stock_list()
        self.update_total_label(total_price)

    def update_total_label(self, total=None):
        if total is None:
            total = sum(product.price * quantity for product, quantity in self.parent.cart)
        self.total_label.setText(f"Total: R$ {total:.2f}")