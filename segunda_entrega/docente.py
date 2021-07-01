# classe Docente
# string nome
# string departamento
# lista  index turmas

class Docente():
    def __init__(self, nome, departamento, turmas):
        self.nome = nome[0:20]
        self.departamento = departamento[0:40]
        self.turmas = turmas
    
    def __repr__(self):
        return f"{self.nome.ljust(20)}  {self.departamento.ljust(40)}  {self.turmas}"