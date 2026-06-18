class ImpostoMEI:
    def calcular_imposto(self, faturamento):
        return faturamento * 0.02


class ImpostoSimples:
    def calcular_imposto(self, faturamento):
        return faturamento * 0.06


class ImpostoLucroPresumido:
    def calcular_imposto(self, faturamento):
        return faturamento * 0.11


regimes = [
    ImpostoMEI(),
    ImpostoSimples(),
    ImpostoLucroPresumido()
]

faturamento = 10000

for regime in regimes:
    imposto = regime.calcular_imposto(faturamento)
    print(f"Imposto calculado: R$ {imposto:.2f}")