#Main Banco
from app import *
appl = QApplication(sys.argv)
window = Mainwindow() 
window.show()
appl.exec_()