class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
            print("Salário alterado com sucesso.")
        else:
            print("O salário deve ser maior que zero.")

    def mostrar_funcionario(self):
        print(f"Funcionário: {self.nome}")
        print(f"Salário: R$ {self.__salario:.2f}")


funcionario1 = Funcionario("Mariana", 2500)

funcionario1.mostrar_funcionario()

funcionario1.salario = 3000
funcionario1.mostrar_funcionario()

funcionario1.salario = -1000
funcionario1.mostrar_funcionario()