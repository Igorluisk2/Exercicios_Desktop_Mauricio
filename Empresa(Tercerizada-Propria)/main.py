from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication,QPropertyAnimation,QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys
from database import Data_base


class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytax - Sistema de cadastro de empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        
        ######################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)
        ######################################
        
        ######################################
        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        ######################################
        
        self.btn_cadastrar.clicked.connect(self.cadastrar_empresas)

    def leftMenu(self):
        
        width = self.left_menu.width()
        
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9
            
        self.animation = QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()      
    
    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()
        
        '''fullDataSet = (
            
            self.txt_cnpj.(),self.txt_nome.text(),self.txt_logradouro.text(),self.
        )'''
       
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()