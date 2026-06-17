class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo_novo):
        if saldo_novo == "":
            print("O SALDO NÃO PODE ESTAR VAZIO.")
        elif saldo_novo < 0:
            print("O SALDO PODE SER MENOR QUE 0")
        else:
            self.__saldo = saldo_novo
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular_novo):
        if (titular_novo ==  ""):
            print(f"Campo vazio, defina um nome")
        else:
            self.__titular = titular_novo 


conta1 = ContaBancaria("Ana", 100)

conta1.saldo = 500
conta1.__titular = "jorge"

print(conta1.saldo)
print(conta1.__titular)
