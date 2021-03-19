class Aluno:
    """Tentando modelar classe aluno"""

    def __init__(self, nome, idade, curso, ano):  # construtor da classe
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ano = ano

    def mostrar_aluno(self):
        print(self.nome, " ", self.idade, " ", self.curso, " ", self.ano)


class Academico(Aluno):
    """Modelar uma classe filha academico"""

    def __init__(self, nome, idade, curso, ano):
        super().__init__(nome, idade, curso, ano)
        self.tcc = 'Em andamento'

    def mostrar_aluno(self):
        print(self.nome, " ", self.idade, "", self.curso, "", self.ano, " ", self.tcc)


acad01 = Academico(nome='Ceblinha', idade=18, curso='Computação', ano=2018)
acad01.mostrar_aluno()
