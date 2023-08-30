import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTabWidget, QComboBox, QWidget
from cadastrar import CadastroTab, Funcionarios
from estoque import EstoqueTab
'''from vendas import VendasTab'''

class MercadoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.funcionarios = []
        self.carrinho = []

        self.setWindowTitle("Sistema de Cadastro de Pessoal")
        self.setGeometry(100, 100, 800, 600)

        self.abas = QTabWidget()
        self.aba_cadastro_interno = CadastroTab(self)
        self.aba_cadastro_terceirizado = CadastroTab(self)
        self.aba_estoque = EstoqueTab(self)
        '''self.aba_vendas = VendasTab(self)'''

        self.abas.addTab(self.aba_cadastro_interno, "Cadastro Interno")
        self.abas.addTab(self.aba_cadastro_terceirizado, "Cadastro Terceirizado")
        self.abas.addTab(self.aba_estoque, "Estoque")
        '''self.abas.addTab(self.aba_vendas, "Vendas")'''

        self.iniciar_interface()

    def iniciar_interface(self):
        layout = QVBoxLayout()
        layout.addWidget(self.abas)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def cadastrar_funcio(self):
        nome = self.aba_cadastro_interno.entrada_nome.text()
        horast = float(self.aba_cadastro_interno.entrada_horast.text())
        vhora = float(self.aba_cadastro_interno.entrada_vhora.text())

        funcio = funcio(nome, horast, vhora)
        self.funcionarios.append(funcio)

        self.aba_estoque.atualizar_lista_estoque()
        ''' self.aba_vendas.atualizar_combo_produto()
        self.aba_vendas.atualizar_rotulo_horast(self.aba_vendas.combo_produto.currentIndex())'''
        self.aba_cadastro_interno.limpar_campos()

        self.aba_cadastro_interno.rotulo_mensagem_cadastro.setText("Cadastro realizado com sucesso!")

    def vender_funcionarios(self):
        total_horast = 0.0
        for funcio, vhora in self.carrinho:
            if vhora > funcio.vhora:
                '''self.aba_vendas.lista_vendas.addItem(f"vhoraQuantidade insuficiente para {produto.nome}.")'''
                return

            funcio.vhora -= vhora
            total_horast += funcio.horast * vhora

        self.carrinho = []
        '''self.aba_vendas.atualizar_lista_carrinho()'''
        self.aba_estoque.atualizar_lista_estoque()
        '''self.aba_vendas.atualizar_rotulo_total()'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mercado_app = MercadoApp()
    mercado_app.show()
    sys.exit(app.exec_())
    
#produto = funcio
#produtos = funcionarios
#preco = horast
#quanti = vhora