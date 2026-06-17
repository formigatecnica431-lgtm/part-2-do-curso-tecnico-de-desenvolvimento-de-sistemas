class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço do livro atualizado.")
        else:
            print("O preço do livro deve ser maior que zero.")

    def mostrar_livro(self):
        print(f"Livro: {self.titulo}")
        print(f"Preço: R$ {self.__preco:.2f}")


livro1 = Livro("Python para Iniciantes", 59.90)

livro1.mostrar_livro()

livro1.preco = 79.90
livro1.mostrar_livro()

livro1.preco = 0
livro1.mostrar_livro()