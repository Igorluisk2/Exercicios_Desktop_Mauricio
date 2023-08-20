#Main Banco
from app import *
appl = QApplication(sys.argv)
window = Banco() 
window.show()
appl.exec()