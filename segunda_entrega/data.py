from discente import Discente
from docente import Docente
from materia import Materia
from turmas import Turmas

discentes = [None]
docentes = [None] 
materias = [None] 
turmas = [None] 

def criarDadosTeste():
    discentes = [None] * 5
    docentes = [None] * 3
    materias = [None] * 3
    turmas = [None] * 4

    discentes[0] = Discente("Pedro Rocha", "120010000", "Engenharia de Produção", [0])
    discentes[1] = Discente("Aline Gomez", "120020000", "Engenharia de Materias", [1, 2])
    discentes[2] = Discente("Diana Castro", "120030000", "Engenharia Nuclear", [1, 3])
    discentes[3] = Discente("Diego Silva", "120040000", "Engenharia de Computação e Eletrônica", [])
    discentes[4] = Discente("Luiza Ferreira", "120050000", "Arquitetura", [0, 4])

    docentes[0] = Docente("Alexa Coelho", "Departamento de Matemática", [0, 1])
    docentes[1] = Docente("Bruno Santos", "Departamento de Expressão Gráfica", [2])
    docentes[2] = Docente("Johan Carvalho", "Departamento de Expressão Gráfica", [3])

    materias[0] = Materia("Cálculo I", [0])
    materias[1] = Materia("Cálculo II", [1])
    materias[2] = Materia("Desenho Técnico", [2, 3])

    turmas[0] = Turmas("Cálculo I", "Alexa Coelho", ["120010000", "120050000"], [])
    turmas[1] = Turmas("Cálculo II", "Alexa Coelho", ["120020000", "120030000"], [])
    turmas[2] = Turmas("Desenho Técnico", "Bruno Santos", ["120020000"], [])
    turmas[3] = Turmas("Desenho Técnico", "Johan Carvalho", ["120030000", "120050000"], [])

    return discentes, docentes, materias, turmas

def testarDados(discentes, docentes, materias, turmas):
    for discente in discentes:
        print(discente)

    for docente in docentes:
        print(docente)

    for materia in materias:
        print(materia)

    for turma in turmas:
        print(turma)