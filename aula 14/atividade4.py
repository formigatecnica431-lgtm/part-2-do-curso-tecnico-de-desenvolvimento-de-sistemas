class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço alterado com sucesso.")
        else:
            print("O preço deve ser maior que zero.")

    def mostrar_produto(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.__preco:.2f}")


produto1 = Produto("Mouse", 80)

produto1.mostrar_produto()

produto1.preco = 95
produto1.mostrar_produto()

produto1.preco = -30
produto1.mostrar_produto()