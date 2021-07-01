from discente import Discente
from docente import Docente
from materia import Materia
from turmas import Turmas
from data import criarDadosTeste

discentes, docentes, materias, turmas = criarDadosTeste()

# n[0] -> menu principal
# n[1] -> menu turmas
n = [-1] * 2

while n[0] != 0:

    # input nivel 1
    n[0] = str(input("Escolha uma opcao: "))

    # tratamento do input
    if not n[0].isdigit():
        print("Insira um input valido.")
        continue
    else:
        n[0] = int(n[0])


    # cadastrar nova materia
    if n[0] == 1:
        print("Cadastrar nova matéria")
        nome = input("Insira o nome da matéria: ")
        
        materias.append(Materia(nome, []))

    # cadastrar novo docentes
    elif n[0] == 2:
        print("Cadastrar novo docente")
        nome = input("Insira o nome do docente: ")
        departamento = input("Insira o departamento do docente: ")
        
        docentes.append(Docente(nome, departamento, []))

    # cadastrar novo discente
    elif n[0] == 3:
        print("Cadastrar novo discente")
        nome = input("Insira o nome do discente: ")
        dre = input("Insira o DRE do discente: ")
        curso = input("Insira o curso do discente: ")
        
        discentes.append(Discente(nome, departamento, []))

    # mostrar todas as materias
    elif n[0] == 4:
        print("Matérias")
        print("Nome".ljust(30) + "  " + "Turmas")
        for materia in materias:
            print(materia)

    # mostrar todos os docentes
    elif n[0] == 5:
        print("Docentes")
        print("Nome".ljust(20) + "  " + "Departamento".ljust(40) + "  " + "Turmas")
        for docente in docentes:
            print(docente)

    # mostrar todos os discentes
    elif n[0] == 6:
        print("Discentes")
        print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Curso".ljust(40) + "  " + "Turmas")
        for discente in discentes:
            print(discente)

    # abrir menu turmas
    elif n[0] == 7:

        while n[1] != 0:
            
            # input nivel 2
            n[1] = input(f"Escolha uma segunda opcao {n}: ")

            if not n[1].isdigit():
                print("Insira um input valido.")
                continue
            else:
                n[1] = int(n[1])

            # cadastrar nova turma
            if n[1] == 1:
                """print("Cadastrar nova turma")
                nome = input("Insira o nome da turma: ")
                
                turmas.append(Turmas(nome, []))"""

            # registrar o docente de uma turma
            elif n[1] == 2:
                pass

            # registrar os discentes de uma turma
            elif n[1] == 3:
                pass

            # remover um discente de uma turma
            elif n[1] == 4:
                pass

            # assignar nota final dos alunos de uma turma
            elif n[1] == 5:
                pass

            # mostrar todos os discentes de uma turma (alfabético)
            elif n[1] == 6:
                pass

            # mostrar todas as turmas (número de alunos)
            elif n[1] == 7:
                pass

    
    # fechar programa
    elif n[0] == 0:
        pass
    
    # input invalido
    else:
        pass


"""
turmas = "\n\nTurmas: \n"
for turma in self.turmas:
    turmas += turma + turmas[turma] + "\n"

alunos = "\n\nAlunos: \n"
for aluno in self.alunos:
    alunos += aluno + "\n"

turmas = "\n\nTurmas: \n"
for turma in self.turmas:
    turmas += turma + docentes[turma].nome + "\n"
"""