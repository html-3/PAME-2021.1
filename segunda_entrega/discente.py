# classe Discente
# string nome
# string dre
# string curso
# lista  index turmas cadastradas

class Discente():
    def __init__(self, nome, dre, curso, turmas):
        self.nome = nome[0:20]
        self.dre = dre[0:9]
        self.curso = curso[0:40]
        self.turmas = turmas
    
    def __repr__(self):
        return f"{self.dre.ljust(9)}  {self.nome.ljust(20)} {self.curso.ljust(40)}" 