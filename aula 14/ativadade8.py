class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("A senha deve ter pelo menos 6 caracteres.")

    def mostrar_usuario(self):
        print(f"Usuário: {self.nome}")
        print(self.senha)


usuario1 = Usuario("admin", "123456")

usuario1.mostrar_usuario()

usuario1.senha = "abc"
usuario1.mostrar_usuario()

usuario1.senha = "abc123"
usuario1.mostrar_usuario()