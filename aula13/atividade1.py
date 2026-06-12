class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
class Aluno(Pessoa):
    def __init__(self, nome, idade,ano):
        super().__init__(nome, idade)
        self.ano = ano
        
class Professor(Aluno):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade, ano)