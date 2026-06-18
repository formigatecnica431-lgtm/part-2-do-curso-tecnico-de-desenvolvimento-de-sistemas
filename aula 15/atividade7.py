class NotificacaoEmail:
    def enviar(self, mensagem):
        print(f"E-mail enviado: {mensagem}")


class NotificacaoSMS:
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")


class NotificacaoWhatsApp:
    def enviar(self, mensagem):
        print(f"WhatsApp enviado: {mensagem}")


notificacoes = [
    NotificacaoEmail(),
    NotificacaoSMS(),
    NotificacaoWhatsApp()
]

mensagem = "Seu pedido foi aprovado."

for notificacao in notificacoes:
    notificacao.enviar(mensagem)