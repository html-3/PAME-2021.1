# classe  Turmas
# inteiro materia
# string  docente
# lista   string dre discentes
# lista   notas discentes

class Turmas():
    def __init__(self, materia, docente, alunos):
        self.materia = materia[0:30]
        self.docente = docente[0:20]
        self.alunos = alunos
    
    def __repr__(self):
        return f"{self.materia.ljust(30)}  {self.docente.ljust(20)}"