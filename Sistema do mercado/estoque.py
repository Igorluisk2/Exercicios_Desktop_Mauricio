import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
class StockTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        layout = QVBoxLayout()

        self.stock_list = QListWidget()
        layout.addWidget(self.stock_list)

        self.setLayout(layout)

    def update_stock_list(self):
        self.stock_list.clear()
        for product in self.parent.products:
            self.stock_list.addItem(f"{product.name} - Quantidade: {product.quantity}")