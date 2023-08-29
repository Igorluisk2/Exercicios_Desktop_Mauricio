from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication,QPropertyAnimation,QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
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
        
        fullDataSet = (
            self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(), 
            self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(), self.txt_uf.text(), 
            self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text()
            )
        
        #CADASTRAR NO BD
        resp = db.register_company(fullDataSet)
        
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox. Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as Informações foram preenchidadas corretamente!") 
            msg.exec()
            db.close_connection()
            return    
       
if __name__ == "__main__":
    
    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()
    
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()