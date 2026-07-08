class Cliente ():
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        
    @staticmethod
    def cadastrarcliente(self):
        while True:
            self.nome = input("Digite seu nome:")
            if self.nome == "":
                print("Digite seu nome novamente: ")
            else:
                break
            print("")
            self.cpf = input("digite seu CPF(MAX 11 DIGITOS):")
            if self.cpf == "" or len(self.cpf <= 11):
                print("digita direito bobo")
            else:
                break
            print("")
            self.telefone = input("Digite seu telefone(MAX 9 DIGITOS):")
            if self.telefone == "" or len(self.telefone <= 9):
                print("digita direito bobo")
            else:
                break
            print("")
            self.email = input("Digite seu e-mail:")
            if self.email == "":
                print("Você calado é um poeta")
            else:
                break