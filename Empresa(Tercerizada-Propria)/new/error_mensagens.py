from PySide6.QtWidgets import QMessageBox



class MensagemErro(QMessageBox):
    def __init__(self):
        super().__init__()
        
    def erro_funcionario_pagamento(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("Erro nos dados informados, verifique os campos e tente novamente.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()
    
    def erro_hora_trabalhada(self):
        self.mensagem_erro = QMessageBox()
        self.mensagem_erro.setText("O valor informado é inválido.")
        self.mensagem_erro.setIcon(QMessageBox.Warning)
        self.mensagem_erro.show()