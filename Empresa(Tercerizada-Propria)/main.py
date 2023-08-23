from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys


class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytax - Sistema de cadastro de empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()