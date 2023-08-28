import sqlite3

class Data_base:
    
    def __init__(self, name = "syste,.db") -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_company(self):
        
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresa(
            
            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            
            PRIMARY KEY(CNPJ)
            
                       
                       
                       
                       
            );
            
            """)
            