from classGalpao import Galpao

def cadastrar_novo_galpao():
    print("CADASTRO DE NOVO GALPÃO")
    
    codigo = input("Digite o código do galpão:").strip()

    if not codigo:
        print("CÓDIGO NÃO PODE FICAR VAZIO!")
        return
    
    nome = input("Digite o código do galpão:").strip()

    if not nome:
        print("CÓDIGO NÃO PODE FICAR VAZIO!")
        return
    
    endereco = input("Digite o código do galpão:").strip()

    if not endereco:
        print("CÓDIGO NÃO PODE FICAR VAZIO!")
        return
        
        
    novo_galpao = Galpao(codigo,nome,endereco)

    galpoes.append(novo_galpao)

galpoes = []


while True:
    
    print('''
        BEM VINDO A GALPAX
    
    MENU:
        1. Cadastrar Novo Galpão
        
        0. Sair
''')
    
    
    op = input ("Digite a opção desejada: ")
    
    if op == "1":
        cadastrar_novo_galpao()
    elif op == "0":
        print("Saindo do progama")