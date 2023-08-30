import sys
from Funcionario import *
from error_mensagens import MensagemErro
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QCheckBox


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Pagamento de Funcionários")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.lbl_layout = QVBoxLayout()

        self.lbl_dados_funcionario = QLabel("Digite os dados do funcionário:")
        self.lbl_layout.addWidget(self.lbl_dados_funcionario)

        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText("Nome")
        self.lbl_layout.addWidget(self.txt_nome)

        self.txt_hora = QLineEdit()
        self.txt_hora.setPlaceholderText("Horas Trabalhadas")
        self.lbl_layout.addWidget(self.txt_hora)

        self.txt_valor_por_hora = QLineEdit()
        self.txt_valor_por_hora.setPlaceholderText("Valor por Hora")
        self.lbl_layout.addWidget(self.txt_valor_por_hora)

        self.ck_terceirizado = QCheckBox("Terceirizado")
        self.lbl_layout.addWidget(self.ck_terceirizado)

        self.txt_despesa_adicional = QLineEdit()
        self.txt_despesa_adicional.setPlaceholderText("Despesa Adicional (para funcionários terceirizados)")
        self.lbl_layout.addWidget(self.txt_despesa_adicional)

        self.btn_adicionar = QPushButton("Adicionar Funcionário")
        self.btn_adicionar.clicked.connect(self.adicionar_funcionario)
        self.lbl_layout.addWidget(self.btn_adicionar)

        self.txtb_exibir_texto = QTextBrowser()
        self.lbl_layout.addWidget(self.txtb_exibir_texto)

        self.central_widget.setLayout(self.lbl_layout)

        self.funcionarios = []
      

    def adicionar_funcionario(self):
        try:
            if self.txt_nome.text().isdigit() == True:
                self.erro_mensagem = MensagemErro()
                self.erro_mensagem.erro_funcionario_pagamento()
                
            else:
                terceirizado = self.ck_terceirizado.isChecked()
                despesa_adicional = float(self.txt_despesa_adicional.text()) if terceirizado else 0
                horas_trabalhadas = float(self.txt_hora.text())
                valor_por_hora = float(self.txt_valor_por_hora.text())
                


                if despesa_adicional < 0 or horas_trabalhadas < 0 or valor_por_hora < 0:
                    self.erro_mensagem = MensagemErro()
                    self.erro_mensagem.erro_funcionario_pagamento()


                else:
                
                    nome = self.txt_nome.text()
                    
                    funcionario = Funcionario(nome, horas_trabalhadas, valor_por_hora, terceirizado, despesa_adicional)
                    self.funcionarios.append(funcionario)

                    self.txtb_exibir_texto.append(f"Funcionário adicionado: {funcionario}")
                    
                    self.txt_nome.clear()
                    self.txt_hora.clear()
                    self.txt_valor_por_hora.clear()
                    self.txt_valor_por_hora.clear()
                    self.ck_terceirizado.setChecked(False)
                
        except:
            self.erro_mensagem = MensagemErro()
            self.erro_mensagem.erro_funcionario_pagamento()


        else:
            if self.txt_nome.text().isdigit() == True or despesa_adicional < 0 or horas_trabalhadas < 0 or valor_por_hora < 0:
                pass


            else:
                self.txtb_exibir_texto.append('Pagamento Registrado')
            
                