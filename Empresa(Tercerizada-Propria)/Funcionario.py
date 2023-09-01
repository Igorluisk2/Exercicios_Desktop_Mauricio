class Funcionario:
    def __init__(self, nome, horas_trabalhadas, valor_da_hora, terceirizado, despesa_adicional):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_da_hora = valor_da_hora
        self.terceirizado = terceirizado
        self.despesa_adicional = despesa_adicional
        
        
    def calcular_pagamento(self):
        pagamento = self.horas_trabalhadas * self.valor_da_hora
        if self.terceirizado:
            pagamento += 1.1 * self.despesa_adicional
        return pagamento
    
    
    def __str__(self):
        return f"Nome: {self.nome}, Pagamento: {self.calcular_pagamento()}"