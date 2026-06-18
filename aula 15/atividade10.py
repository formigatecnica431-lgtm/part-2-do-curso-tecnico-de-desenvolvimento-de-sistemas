class ChamadoBaixaPrioridade:
    def calcular_prazo(self):
        return 72


class ChamadoMediaPrioridade:
    def calcular_prazo(self):
        return 24


class ChamadoAltaPrioridade:
    def calcular_prazo(self):
        return 4


chamados = [
    ChamadoBaixaPrioridade(),
    ChamadoMediaPrioridade(),
    ChamadoAltaPrioridade()
]

for chamado in chamados:
    prazo = chamado.calcular_prazo()
    print(f"Prazo de atendimento: {prazo} horas")