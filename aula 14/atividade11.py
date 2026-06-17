class Curso:
    def __init__(self, titulo, carga_horaria):
        self.titulo = titulo
        self.__carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga):
        if nova_carga > 0:
            self.__carga_horaria = nova_carga
            print("Carga horária alterada com sucesso.")
        else:
            print("A carga horária deve ser maior que zero.")

    def mostrar_curso(self):
        print(f"Curso: {self.titulo}")
        print(f"Carga horária: {self.__carga_horaria} horas")


curso1 = Curso("Python POO", 20)

curso1.mostrar_curso()

curso1.carga_horaria = 30
curso1.mostrar_curso()

curso1.carga_horaria = 0
curso1.mostrar_curso()