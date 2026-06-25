class Banco():
    def __init__(self,cliente,saldo,senha,status=False):
        self.cliente = cliente
        self.saldo = saldo
        self.senha = senha
        self.status = status
        
    def login(self):
        while True:
            senha_digitada = input("Digite Senha: ")
            if senha_digitada == self.senha:
                self.status = True
                print("Login ralizado com sucesso!")
                break
            else:
                print("Senha incorreta. tente novamente")
        
    def exibirConta(self):
        if self.status:
            print(f"""
=====DADOS DA CONTA=====
Cliente:{self.cliente}
Saldo: R${self.saldo:.2f}
Status: {self.status}
""")
        else:
            print("acesso negado. Faça login primeiro.")

conta = Banco("Mauro paçoca",2555.52,123456)

conta.login()

conta.exibirConta()
