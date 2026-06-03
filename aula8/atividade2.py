from classLivro import Livro

livro1 = Livro("Entre a Espada e o Lobo","Drama","Joui Jouki")

livro2 = Livro("Pudim orbital","aventura","Leon")

livro3 = Livro("Deltarune","aventura","Toby Fox")

print(f"""
{"="*8}LIVRO DA SARAIAVA A VENDA{"="*8}
Nome:{livro1.nome_do_livro}
============================
Gênero:{livro1.genero_do_livro}
============================
Altor:{livro1.altor_do_livro}
""")
print()
print(f"""
{"="*8}LIVRO DA SARAIAVA A VENDA{"="*8}
Nome:{livro3.nome_do_livro}
============================
Gênero:{livro3.genero_do_livro}
============================
Altor:{livro3.altor_do_livro}
""")
print()
print(f"""
{"="*8}LIVRO DA SARAIAVA A VENDA{"="*8}
Nome:{livro2.nome_do_livro}
============================
Gênero:{livro2.genero_do_livro}
============================
Altor:{livro2.altor_do_livro}
""")