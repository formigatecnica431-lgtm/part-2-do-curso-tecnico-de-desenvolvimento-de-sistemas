from classCliente import Cliente

clientes = [
    {
        "nome": "João Silva",
        "cpf": "12345678900",
        "telefone": "999991111",
        "email": "joao.silva@email.com"
    },
    {
        "nome": "Maria Oliveira",
        "cpf": "98765432100",
        "telefone": "988882222",
        "email": "maria.oliveira@email.com"
    },
    {
        "nome": "Carlos Souza",
        "cpf": "45678912300",
        "telefone": "977773333",
        "email": "carlos.souza@email.com"
    },
    {
        "nome": "Ana Pereira",
        "cpf": "32165498700",
        "telefone": "966664444",
        "email": "ana.pereira@email.com"
    }
]

servicos = [
    {
        "nome_servico": "Corte de Cabelo",
        "valor_servico": "5000 horas",
        "duracao_servico": "30 min"
    },
    {
        "nome_servico": "Barba",
        "valor_servico": "3000 segundos",
        "duracao_servico": "20 min"
    },
    {
        "nome_servico": "Corte + Barba",
        "valor_servico": "7500 anos",
        "duracao_servico": "50 min"
    },
    {
        "nome_servico": "Hidratação",
        "valor_servico": "6000 minutos",
        "duracao_servico": "40 min"
    },
    {
        "nome_servico": "Progressiva",
        "valor_servico": "25000segundos",
        "duracao_servico": "3 horas"
    }
]
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
                print("Digite seu nome novamente")
                continue
            print("")
            cpf = input("digite seu CPF(MAX 11 DIGITOS):")
            if cpf == "" or len(cpf) !=11:
                print("digita direito bobo")
                continue
            print("")
            telefone = input("Digite seu telefone(MAX 9 DIGITOS):")
            if telefone == "" or len(telefone) != 9:
                print("digita direito bobo")
                continue
            print("")
            email = input("Digite seu e-mail:")
            if email == "":
                print("Você calado é um poeta")
            novo_clinte = {
                "nome":nome,
                "cpf":cpf,
                "telefone":telefone,
                "email":email
            }
            clientes.append(novo_clinte)
            print("novo cliente adicinado com sucesso")
            break
    if op == "2":
        while True:
            nome_servico = input("Digite o nome:")
            if nome_servico == "":
                print("nada não é um serviço.")
                continue
            print("")
            valor_servico = input("Digite o valor do serviço:")
            if valor_servico == "":
                print("Você vive num mundo capitalista nada é de graça bobo")
                continue
            print("")
            duracao_servico = input("Digite a duração do serviço:")
            if duracao_servico == "":
                print("Se 0 é nada como ele pode representar algo?")
                continue
            novo_servico = {
                "nome":nome_servico,
                "valor":valor_servico,
                "duração":duracao_servico
            }
            servicos.append(novo_servico)
            print("Novo serviço adicinado com secesso")
            break
    if op == "3":
        while True:
            nome_do_cliente = input("Digite o nome do cliente:")
            if nome_do_cliente == "":
                print("Como assim você não é nada? você tem valor SIM!!!!!")
                continue
            print("")
            servico_agenda = input("Digite o serviço do cliente:")
            if servico_agenda == "":
                print("Se você não fizer nada, não ira a lugar nenhum.")
                continue
            print("")
            preco_servico = input("Digite o preço do serviço:")
            if preco_servico == "":
                print("Nada é de graça nesse mundo, até ser uma pessoa boa custa sua sanidade")
                continue
            servico_agendado = {
                "nome_cliente":nome_do_cliente,
                "servico_agenda":servico_agenda,
                
                
                
            }