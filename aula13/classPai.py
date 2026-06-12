class Pai:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def infor_pai(self):
        print(f"""
Olá meu nome é {self.nome} tenho {self.idade}.
""")
class Filha(Pai):
    def __init__(self, nome, idade,ano,comida):
        super().__init__(nome, idade)
        self.ano = ano
        self.comida = comida
    def infor_filha(self):
        print(f"""
Olá meu nome é {self.nome} tenho {self.idade} faço o {self.ano}
minha comida favorita {self.comida}.
""")