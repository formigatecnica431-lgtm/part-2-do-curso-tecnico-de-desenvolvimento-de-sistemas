class Aluno ():
    def __init__(self,nome,matricola,curso,notas):
        self.nome = nome
        self.matricola = matricola
        self.curso = curso
        self.notas = notas
    def exibir_informacoes(self):
        print(f"""
{"="*8}Detalhes do aluno{"="*8}
Nome:{self.nome}
Matricola:{self.matricola}
Curso:{self.curso}
Notas:{self.notas}
{"="*20}
""")
    def aprovado_reprovado(self):
        if self.notas >= 7 and self.notas <= 10:
            print(f"Olá {self.nome} sua nota é {self.notas}, ou seja você está APROVADO!!!!!.")
        elif self.notas < 7 and self.notas >= 0:
            print(f"Olá {self.nome} sua nota é {self.notas}, ou seja você está REPROVADO MORRA!!!!!")
        elif self.notas > 10:
            print("pane no sistema alguem me desconfigurou MOTIVO: NOTA MAIOR QUE 10")
        elif self.notas < 0:
            print("pane no sistema alguem me desconfigurou MOTIVO: MENOR QUE ZERO")
        else:
            pass