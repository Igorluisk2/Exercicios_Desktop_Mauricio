from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QFormLayout, QWidget
from PySide6.QtCore import (QSize)
from PySide6.QtGui import (QIcon,QPixmap)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QToolButton)
import sys

class CPFWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nome = "CPF MAIN"
        self.setWindowTitle('CPF')
        self.setFixedSize(QSize(300, 180))

        self.cpf_Button = QPushButton('CPF', self)
        self.cpf_Button.setIcon(QIcon('cpf'))
        self.cpf_Button.setGeometry(60, 30, 70, 60)

        self.setup_ui()

    def setup_ui(self):
        self.nome = QLineEdit(self)
        self.renda = QLineEdit(self)
        self.saude = QLineEdit(self)
        self.calcular_button = QPushButton('CALCULAR IMPOSTO', self)

        self.pagina = QFormLayout(self)
        self.pagina.addRow('Nome ', self.nome)
        self.pagina.addRow('Renda ', self.renda)
        self.pagina.addRow('Saúde ', self.saude)
        self.pagina.addRow(self.calcular_button)

        widgetFormulario = QWidget()
        widgetFormulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFormulario)

        self.cpf_Button.deleteLater()

        self.calcular_button.clicked.connect(self.calcular_cpf)

    def calcular_cpf(self):
        renda = int(self.renda.text())
        saude = int(self.saude.text())
        
        if renda>=0 and renda<=20000 and saude==0:
            imposto=renda*(0.15)
            imposto_str=str(imposto)
            
        elif renda>=0 and renda<=20000 and saude>0:
            imposto=renda*(0.15)-saude*(0.5)
            imposto_str=str(imposto)
            
        elif renda>20000 and saude>0:
            imposto=renda*(0.25)-saude*(0.5)
            imposto_str=str(imposto)
        
        elif renda>20000 and saude==0:
            imposto=renda*(0.25)
            imposto_str=str(imposto)
        
        else:
            imposto_str=('VALOR INVÁLIDO')

        self.Qlabel_imposto = QLabel(self)
        self.Qlabel_imposto.setText(imposto_str)

        self.pagina.addRow('Imposto a pagar\n R$ ', self.Qlabel_imposto)

        widgetFormulario = QWidget()
        widgetFormulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFormulario)