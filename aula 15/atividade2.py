class FreteTerrestre:
    def calcular_frete(self, peso, distancia):
        valor = peso * distancia * 0.05
        return valor


class FreteAereo:
    def calcular_frete(self, peso, distancia):
        # Crie uma regra usando peso, distancia e taxa 0.12
        valor = peso * distancia * 0.12
        return valor


class RetiradaLoja:
    def calcular_frete(self, peso, distancia):
        # Retirada na loja não possui custo de frete
        valor = peso * distancia * 0
        return valor


fretes = [
    FreteTerrestre(),
    FreteAereo(),
    RetiradaLoja()
]

for frete in fretes:
    valor_frete = frete.calcular_frete(10, 100)
    print(f"Valor do frete: R$ {valor_frete:.2f}")