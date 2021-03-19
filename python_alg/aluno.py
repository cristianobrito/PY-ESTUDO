class Aluno:
    """Tentando modelar classe aluno"""

    def __init__(self, nome, idade):  # construtor da classe
        self.nome = nome
        self.idade = idade

    def mostrar_aluno(self):
        print(self.nome + " " + self.idade)


aluno01 = Aluno('Maria', str(9))
aluno01.mostrar_aluno()
aluno02 = Aluno("João", str(10))
aluno02.mostrar_aluno()








