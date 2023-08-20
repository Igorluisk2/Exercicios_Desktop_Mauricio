import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class BankApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.account_data = {}
        
        self.setWindowTitle("Bank Application")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_name = QLabel("Name:")
        self.layout.addWidget(self.label_name)
        self.line_edit_name = QLineEdit()
        self.layout.addWidget(self.line_edit_name)

        self.label_account_number = QLabel("Account Number:")
        self.layout.addWidget(self.label_account_number)
        self.line_edit_account_number = QLineEdit()
        self.layout.addWidget(self.line_edit_account_number)

        self.label_initial_balance = QLabel("Initial Balance:")
        self.layout.addWidget(self.label_initial_balance)
        self.line_edit_initial_balance = QLineEdit()
        self.layout.addWidget(self.line_edit_initial_balance)

        self.btn_register = QPushButton("Register Account")
        self.btn_register.clicked.connect(self.register_account)
        self.layout.addWidget(self.btn_register)

        self.btn_deposit = QPushButton("Deposit")
        self.btn_deposit.clicked.connect(self.deposit)
        self.layout.addWidget(self.btn_deposit)

        self.btn_withdraw = QPushButton("Withdraw")
        self.btn_withdraw.clicked.connect(self.withdraw)
        self.layout.addWidget(self.btn_withdraw)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.central_widget.setLayout(self.layout)

    def register_account(self):
        account_number = self.line_edit_account_number.text()
        if account_number in self.account_data:
            self.status_label.setText("Account number already registered.")
        else:
            name = self.line_edit_name.text()
            initial_balance = float(self.line_edit_initial_balance.text())
            self.account_data[account_number] = {
                "name": name,
                "balance": initial_balance
            }
            self.status_label.setText("Account registered successfully.")

    def deposit(self):
        account_number = self.line_edit_account_number.text()
        if account_number in self.account_data:
            amount = float(input("Enter deposit amount: "))
            self.account_data[account_number]["balance"] += amount
            self.status_label.setText("Deposit successful.")
        else:
            self.status_label.setText("Account not found.")

    def withdraw(self):
        account_number = self.line_edit_account_number.text()
        if account_number in self.account_data:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= self.account_data[account_number]["balance"]:
                self.account_data[account_number]["balance"] -= amount
                self.status_label.setText("Withdrawal successful.")
            else:
                self.status_label.setText("Insufficient balance.")
        else:
            self.status_label.setText("Account not found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    sys.exit(app.exec_())
