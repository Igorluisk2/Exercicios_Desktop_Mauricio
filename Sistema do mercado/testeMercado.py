import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class MarketApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.products = []
        self.cart = []

        self.setWindowTitle("Mercadinho Do Senac")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.tab_register = QWidget()
        self.tab_stock = QWidget()
        self.tab_sales = QWidget()

        self.tabs.addTab(self.tab_register, "Cadastro")
        self.tabs.addTab(self.tab_stock, "Estoque")
        self.tabs.addTab(self.tab_sales, "Vendas")

        self.init_ui()

    def init_ui(self):
        self.init_register_tab()
        self.init_stock_tab()
        self.init_sales_tab()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def init_register_tab(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.quantity_input = QLineEdit()

        register_button = QPushButton("Cadastrar")
        register_button.clicked.connect(self.register_product)

        layout.addWidget(QLabel("Nome do Produto:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Preço Unitário:"))
        layout.addWidget(self.price_input)
        layout.addWidget(QLabel("Quantidade em Estoque:"))
        layout.addWidget(self.quantity_input)
        layout.addWidget(register_button)

        self.register_message_label = QLabel()
        layout.addWidget(self.register_message_label)

        self.tab_register.setLayout(layout)

    def init_stock_tab(self):
        layout = QVBoxLayout()

        self.stock_list = QListWidget()
        layout.addWidget(self.stock_list)

        self.tab_stock.setLayout(layout)

    def init_sales_tab(self):
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

        self.tab_sales.setLayout(layout)

    def register_product(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())

        product = Product(name, price, quantity)
        self.products.append(product)

        self.update_stock_list()
        self.update_product_combobox()
        self.update_cart_list()
        self.update_total_label(0)  # Reset the total label

        self.register_message_label.setText("Produto cadastrado com sucesso!")

    def update_stock_list(self):
        self.stock_list.clear()
        for product in self.products:
            self.stock_list.addItem(f"{product.name} - Quantidade: {product.quantity}")

    def update_product_combobox(self):
        self.product_combobox.clear()
        for product in self.products:
            self.product_combobox.addItem(product.name)

    def update_price_label(self, index):
        if index >= 0 and index < len(self.products):
            product = self.products[index]
            self.price_label.setText(f"Preço: R$ {product.price:.2f}")

    def add_to_cart(self):
        product_index = self.product_combobox.currentIndex()
        product = self.products[product_index]
        quantity = int(self.quantity_input_sales.text())

        if quantity > product.quantity:
            self.sales_list.addItem("Quantidade insuficiente em estoque.")
            return

        self.cart.append((product, quantity))
        self.update_cart_list()
        self.update_total_label()

    def update_cart_list(self):
        self.cart_list.clear()
        for product, quantity in self.cart:
            self.cart_list.addItem(f"{product.name} - Quantidade: {quantity}")

    def sell_products(self):
        total_price = 0.0
        for product, quantity in self.cart:
            if quantity > product.quantity:
                self.sales_list.addItem(f"Quantidade insuficiente para {product.name}.")
                return

            product.quantity -= quantity
            total_price += product.price * quantity

        self.cart = []
        self.update_cart_list()
        self.update_stock_list()
        self.update_total_label(total_price)

    def update_total_label(self, total=None):
        if total is None:
            total = sum(product.price * quantity for product, quantity in self.cart)
        self.total_label.setText(f"Total: R$ {total:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    market_app = MarketApp()
    market_app.show()
    sys.exit(app.exec_())
