class RelatorioPDF:
    def gerar(self, dados):
        print(f"Gerando relatório PDF com os dados: {dados}")


class RelatorioExcel:
    def gerar(self, dados):
        print(f"Gerando relatório Excel com os dados: {dados}")


class RelatorioHTML:
    def gerar(self, dados):
        print(f"Gerando relatório HTML com os dados: {dados}")


relatorios = [
    RelatorioPDF(),
    RelatorioExcel(),
    RelatorioHTML()
]

dados = "Vendas do mês"

for relatorio in relatorios:
    relatorio.gerar(dados)