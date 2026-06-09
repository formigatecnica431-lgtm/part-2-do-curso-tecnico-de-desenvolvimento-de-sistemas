class Produto():
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def valor_total(self):
        valor_produto = self.preco * self.quantidade
        return valor_produto
        
    def aplicar_desconto(self,percentual):
        