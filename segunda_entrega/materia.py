# classe Materia
# string nome
# lista  index turmas

class Materia():
    def __init__(self, nome, turmas):
        self.nome = nome[0:30]
        self.turmas = turmas

    def __repr__(self):
        return f"{self.nome.ljust(30)}  {self.turmas}"