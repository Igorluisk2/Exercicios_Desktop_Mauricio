import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class RegisterTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

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

        self.setLayout(layout)

    def register_product(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())

        product = Product(name, price, quantity)
        self.parent.products.append(product)

        self.parent.tab_stock.update_stock_list()
        self.parent.tab_sales.update_product_combobox()
        self.parent.tab_sales.update_cart_list()
        self.parent.tab_sales.update_total_label(0)  # Reset the total label

        self.register_message_label.setText("Produto cadastrado com sucesso!")
