class Animais:
    def __init__(self):
        print(f"sons dos animais")

class Cachorro: 
    def somdoanimal(self):
        print(f"o cachorro faz au au")
        

class Gato:
    def somdoanimal(self):
        print(f"O gato faz miau")
        

class Vaca:
    def somdoanimal(self):
        print(f"A vaca faz muuuuuuuu")
        

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

cachorro.somdoanimal()
gato.somdoanimal()
vaca.somdoanimal()

Animais()
animais = [Cachorro(),Gato(),Vaca()]

for animal in animais:
    animal.somdoanimal()