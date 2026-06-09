class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def mostrar_informcoes_pessoa(self):
        print(f"""
Olá meu nome é {self.nome}, minha idade é {self.idade}.
Eu gosto de morangos de chocolate.
""")



    def fazer_aniversario(self):
        self.idade += 1
        print(f"No meu anivesario vou fazer {self.idade}, espero ganhar morangos de chocolate.")