import sys
import typing
import PySide2.QtCore
from PySide2.QtWidgets import QApplication,QLabel,QWidget,QMainWindow,QVBoxLayout,QToolBar,QAction
from PySide2.QtGui import QPixmap
from vendas import Vendas
from cadastroProduto import Cadastro
from estoque import Estoque
class Mercado(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mercado Senac")
        self.setFixedSize(800,600)
        
        #Centralizando widgets 
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        #Criando um Layout Vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        #Criando a ToolBar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        #Colocando uma imagem na tela principal
        lbl_img = QLabel()
        lbl_img.setPixmap(QPixmap())
        
        
        
app = QApplication()
janela = Mercado()
janela.show()
app.exec_()