from classAluno import Aluno

aluno1 = Aluno("Lucas",35,1,[7,8,8.5,9],"A")

aluno2 = Aluno("Jorge",25,8,[5.5,9,1.5,6],"B")

aluno3 = Aluno("tais",32,6,[9,8.5,7,9.10],"C")

print(f"""
{"="*8}FICHA ALUNO{"="*8}
Nome do aluno:{aluno1.nome}
Idade do aluno:{aluno1.idade}
Turma do aluno:{aluno1.turma}
Notas do aluno:{aluno1.notas}
{"="*16}
""")
print()
print(f"""
{"="*8}FICHA ALUNO{"="*8}
Nome do aluno:{aluno2.nome}
Idade do aluno:{aluno2.idade}
Turma do aluno:{aluno2.turma}
Notas do aluno:{aluno2.notas}
{"="*16}
""")
print()
print(f"""
{"="*8}FICHA ALUNO{"="*8}
Nome do aluno:{aluno3.nome}
Idade do aluno:{aluno3.idade}
Turma do aluno:{aluno3.turma}
Notas do aluno:{aluno3.notas}
{"="*16}
""")

