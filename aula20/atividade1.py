from classCliente import Cliente

clientes = []
servicos = []
agendamento = []
while True:
    print("""
======== SALÃO DE BELEZA ========
1 - Cadastrar Cliente
2 - Cadastrar Serviço
3 - Agendar Atendimento
4 - Listar Agendamentos
5 - Cancelar Agendamento
0 - Sair
=================================
""")
    
    op = input("Escolha uma opção:")
    
    if op == "1":
        while True:
            nome = input("Digite seu nome:")
            if nome == "":
                print("Digite seu nome novamente: ")
                continue
            print("")
            cpf = input("digite seu CPF(MAX 11 DIGITOS):")
            if cpf == "" or len(cpf <= 11):
                print("digita direito bobo")
                continue
            print("")
            telefone = input("Digite seu telefone(MAX 9 DIGITOS):")
            if telefone == "" or len(telefone <= 9):
                print("digita direito bobo")
                continue
            print("")
            email = input("Digite seu e-mail:")
            if email == "":
                print("Você calado é um poeta")
                continue
            
            novo_cliente = Cliente()