class Produto():
    def __init__(self,nome,preco,quantidade):
        self.nome =  nome
        self.preco = preco
        self.quantidade = quantidade
        
    def valor_total(self):
        valor_total_produto = self.preco * self.quantidade
        print(f"Seu valor total é {valor_total_produto}")
        
    def valor_desconto(self,percentual):
        self.preco -= self.preco * percentual / 100
        
    def mostrar_dados(self):
        print(f"""
{"="*20}Nota fiscal{"="*20}
| Produto:{self.nome}
| Valor Total:{self.preco}
| Quantidade:{self.quantidade}
{"="*51}
""")