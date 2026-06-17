class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def mostrar_conta(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("João", 500)

conta1.mostrar_conta()

conta1.depositar(200)
conta1.sacar(100)

print(conta1.saldo)

conta1.sacar(1000)
conta1.mostrar_conta()