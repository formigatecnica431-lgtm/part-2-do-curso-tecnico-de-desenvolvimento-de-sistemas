class PagamentoPix:
    def pagar(self, valor):
        print(f"Pagamento via Pix realizado no valor de R$ {valor:.2f}.")


class PagamentoCartao:
    def pagar(self, valor):
        # Complete a mensagem de pagamento no cartão
        print(f"Pagamento via cartão realizado no valor de R$ {valor:.2f}.")


class PagamentoBoleto:
    def pagar(self, valor):
        # Complete a mensagem de boleto
        print(f"Pagamento via boleto realizado no valor de R$ {valor:.2f}.")


pagamentos = [
    PagamentoPix(),
    PagamentoCartao(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.pagar(250)