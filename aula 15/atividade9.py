class PedidoLojaFisica:
    def processar_pedido(self, numero_pedido):
        print(f"Pedido {numero_pedido} separado no balcão.")


class PedidoOnline:
    def processar_pedido(self, numero_pedido):
        print(f"Pedido {numero_pedido} separado para envio.")


class PedidoMarketplace:
    def processar_pedido(self, numero_pedido):
        print(f"Pedido {numero_pedido} enviado para validação do externa.")


pedidos = [
    PedidoLojaFisica(),
    PedidoOnline(),
    PedidoMarketplace()
]

for pedido in pedidos:
    pedido.processar_pedido(1025)