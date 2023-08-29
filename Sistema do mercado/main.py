import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
from cadastroProduto import Product,RegisterTab
from estoque import StockTab
from vendas import SalesTab
class MarketApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.products = []
        self.cart = []

        self.setWindowTitle("Mercadinho Senac")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()

        self.init_ui()

    def init_ui(self):
        self.tab_register = RegisterTab(self)
        self.tab_stock = StockTab(self)
        self.tab_sales = SalesTab(self)

        self.tabs.addTab(self.tab_register, "Cadastro")
        self.tabs.addTab(self.tab_stock, "Estoque")
        self.tabs.addTab(self.tab_sales, "Vendas")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    market_app = MarketApp()
    market_app.show()
    sys.exit(app.exec_())