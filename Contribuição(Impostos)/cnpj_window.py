from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QFormLayout, QWidget
from PySide6.QtCore import (QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QToolButton)
import sys

class CNPJWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CNPJ')
        self.setFixedSize(QSize(300, 180))

        self.cnpj_Button = QPushButton('CNPJ', self)
        self.cnpj_Button.setIcon(QIcon('cnpj'))
        self.cnpj_Button.setGeometry(160, 30, 70, 60)

        self.setup_ui()

    def setup_ui(self):
        self.nome = QLineEdit(self)
        self.renda = QLineEdit(self)
        self.qta_funcionario = QLineEdit(self)
        self.calcular_button_cnpj = QPushButton('CALCULAR IMPOSTO', self)

        self.pagina = QFormLayout(self)
        self.pagina.addRow('Nome ', self.nome)
        self.pagina.addRow('Renda ', self.renda)
        self.pagina.addRow('Número de funcionários ', self.qta_funcionario)
        self.pagina.addRow(self.calcular_button_cnpj)

        widgetFormulario = QWidget()
        widgetFormulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFormulario)

        self.cnpj_Button.deleteLater()

        self.calcular_button_cnpj.clicked.connect(self.calcular_cnpj)

    def calcular_cnpj(self):
        renda = int(self.renda.text())
        funcionario = int(self.qta_funcionario.text())
        
        if funcionario>=0 and funcionario<10:
            imposto=renda*(0.16)
            imposto_str=int(imposto)
        
        elif funcionario>=10:
            imposto=renda*(0.14)
            imposto_str=str(imposto)
        
        else:
            imposto_str=('VALOR INVÁLIDO')

        self.Qlabel_imposto = QLabel(self)
        self.Qlabel_imposto.setText(imposto_str)

        self.pagina.addRow('Imposto a pagar R$ ', self.Qlabel_imposto)

        widgetFormulario = QWidget()
        widgetFormulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFormulario)