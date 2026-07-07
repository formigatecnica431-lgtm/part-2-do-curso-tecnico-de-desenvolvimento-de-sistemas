class Carro ():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        
    
    
    def descrever_carro(self):
        print(f"""
{"="*20}
CARRO DESCRIÇÃO
Marca:{self.marca}
modelo:{self.modelo}
{"="*20}
""")
