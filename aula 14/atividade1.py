class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome

pessoa1 = Pessoa("JOÃO PAULO")
print(pessoa1.nome)