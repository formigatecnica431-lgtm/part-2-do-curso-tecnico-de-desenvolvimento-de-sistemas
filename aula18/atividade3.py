from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20


class Vendedor(Funcionario):
    def calcular_bonus(self):
        # Vendedor recebe 10%
        return self.salario * 0.10


class Estagiario(Funcionario):
    def calcular_bonus(self):
        # Estagiário recebe 5%
        return self.salario * 0.5


funcionarios = [
    Gerente("Ana", 5000),
    Vendedor("Carlos", 3000),
    Estagiario("Mariana", 1200)
]

for funcionario in funcionarios:
    bonus = funcionario.calcular_bonus()
    print(f"{funcionario.nome} receberá R$ {bonus:.2f} de bônus.")