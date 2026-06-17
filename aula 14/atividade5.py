class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova_nota):
        if nova_nota <= 10 and nova_nota >= 0:
            self.__nota = nova_nota
            print("Nota alterada com sucesso.")
        else:
            print("A nota deve estar entre 0 e 10.")

    def mostrar_aluno(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.__nota}")


aluno1 = Aluno("Carlos", 8)

aluno1.mostrar_aluno()

aluno1.nota = 9.5
aluno1.mostrar_aluno()

aluno1.nota = 15
aluno1.mostrar_aluno()