class Pokemon():
    def __init__(self,nome_pokemon,tipo_pokemon,passiva_pokemon):
        self.nome_do_pokemon = nome_pokemon
        self.tipo_do_pokemon = tipo_pokemon
        self.passiva_do_pokemon = passiva_pokemon
    
    def mostrar_informacoes_pokemon(self):
        print(f"""
{"="*10}POKÉMON INFORMAÇÕES{"="*10}
NOME:{self.nome_do_pokemon}
===================================
TIPO:{self.tipo_do_pokemon}
===================================
PASSIVA:{self.passiva_do_pokemon}
===================================
""")