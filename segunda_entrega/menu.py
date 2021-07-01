from discente import Discente
from docente import Docente
from materia import Materia
from turmas import Turmas
from data import criarDadosTeste

discentes, docentes, materias, turmas = criarDadosTeste()

# listagem de alunos duma turma nao eh alfabetica
# listagem de turmas nao eh feita por tamanho
# remocao de docentes, turmas, materias, discentes da database nao implementada
# base de dados existe apenas enquanto o codigo roda, nao e salvo em outro documento
# menu pode ser mais legivel e melhor comentado
# base de dados sao listas de instancias de classe

# n[0] -> menu principal
# n[1] -> menu turmas
# n[2] -> escolher turma
n = [-1] * 3

opcoes = (("Sair do Programa",
           "Cadastro de uma nova matéria",
           "Cadastro de um novo professor",
           "Cadastro de um novo aluno",
           "Mostrar todos as matérias cadastradas",
           "Mostrar todos os professores cadastrados",
           "Mostrar todos os alunos cadastrados",
           "Abrir Menu de Turmas"),
          ("Voltar ao Menu Principal",
           "Cadastro de uma nova turma",
           "Designar professor para uma turma",
           "Adicionar alunos em uma turma",
           "Remover alunos de uma turma",
           "Dar a nota final dos alunos de uma turma",
           "Mostrar todos os alunos de uma turma",
           "Mostras todas as turmas cadastradas")
         )

# input para navegar o menu
def intInput(x):
    print("------------------------------------------------------------------------------------")
    for opcao in opcoes[x]:
        print(opcoes[x].index(opcao), opcao)
    n[x] = input("Escolha uma opcao: ")

    if not n[x].isdigit():
        print("Insira um input valido.")
        n[x] = -1
    else:
        n[x] = int(n[x])

# input para escolher a turma
def turmaInput():
    print("ID  " + "Matéria".ljust(30) + "  " + "Docente".ljust(20))
    for turma in turmas:
        print(turmas.index(turma), "  ", turma)

    while type(n[2]) == int:
        n[2] = input("Escolha um ID de turma: ") 
        if not n[2].isdigit():
            print("Insira um input valido.")
            n[2] = -len(turmas)
        else:
            n[2] = int(n[2])
            if n[2] in range(len(turmas)):
                break
            else:
                n[2] = -len(turmas)
                print("Insira um ID valido.")
                continue

    return n[2]


while n[0] != 0:

    # input nivel 1
    intInput(0)

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
            intInput(1)

            # cadastrar  nova turma
            if n[1] == 1:
                print("Cadastrar nova turma")
                materia = input("Insira a materia da turma: ")
                
                turmas.append(Turmas(materia, "", [], []))

            # registrar o docente de uma turma
            elif n[1] == 2:
                print("Assignar docente")
                
                # escolhar turma
                turmaEscolhida = turmaInput()

                print("Nome".ljust(20) + "  " + "Departamento".ljust(40) + "  " + "Turmas")
                for docente in docentes:
                    print(docente)
                
                while True:
                    docenteEscolhido = input("Insira o docente da turma: ")

                    for docente in docentes:
                        # unico docente
                        try:
                            docente.turmas.remove(turmaEscolhida)
                        except ValueError:
                            pass

                        if docenteEscolhido == docente.nome:
                            turmas[turmaEscolhida].docente = docenteEscolhido
                            docente.turmas.append(turmaEscolhida)
                            n[1] = -1

                    if n[1] == 2:
                        print("Insira o docente valido.")
                    else:
                        break

            # registrar os discentes de uma turma
            elif n[1] == 3:
                print("Matricular Discente")

                # escolhar turma
                turmaEscolhida = turmaInput()
                
                print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Curso".ljust(40) + "  " + "Turmas")
                for discente in discentes:
                    print(discente)

                while True:
                    dreEscolhido = input("Insira o DRE do aluno: ")

                    for discente in discentes:

                        if dreEscolhido == discente.dre:

                            # um aluno nao pode estar duas vezes inscrito numa turma
                            try:
                                discente.turmas.index(turmaEscolhida)
                                break

                            except ValueError:
                                turmas[turmaEscolhida].alunos.append(dreEscolhido)
                                discente.turmas.append(turmaEscolhida)
                            n[1] = -1

                    if n[1] == 3:
                        print("Insira o DRE de um discente valido.")

                    else:
                        break

            # remover um discente de uma turma
            elif n[1] == 4:
                print("Remover Discente")

                # escolhar turma
                turmaEscolhida = turmaInput()

                print(turmas[turmaEscolhida].materia, "-", turmaEscolhida)
                print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Curso".ljust(40) + "  " + "Turmas")
                for discente in discentes:
                    if discente.dre in turmas[turmaEscolhida].alunos:
                        print(discente)

                while True:
                    dreEscolhido = input("Insira o DRE do aluno a ser removido: ")

                    for discente in discentes:
                        if dreEscolhido == discente.dre:
                            try:
                                # remover nota e dre do aluno
                                discente.turmas.remove(turmaEscolhida)
                                indexAluno = turmas[turmaEscolhida].alunos.index(dreEscolhido)
                                turmas[turmaEscolhida].alunos.pop(indexAluno)
                                turmas[turmaEscolhida].notas.pop(indexAluno)
                                n[1] = -1
                            
                            except ValueError:
                                pass

                            break

                    if n[1] == 4:
                        print("Insira o DRE de um discente valido.")

                    else:
                        break

            # assignar nota final dos alunos de uma turma
            elif n[1] == 5:
                print("Notas Finais da Turma")
                
                # escolhar turma
                turmaEscolhida = turmaInput()

                print("Notas de", turmas[turmaEscolhida].materia, "-", turmaEscolhida)
                print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Nota")
                for discente in discentes:
                    if discente.dre in turmas[turmaEscolhida].alunos:
                        while n[1] == 5:
                            nota = input(f"{discente.dre}  {discente.nome.ljust(20)}  ")

                            try:
                                nota = round(float(nota), 1)
                                if not 10.0 >= nota >= 0.0:
                                    print("Nota final invalida.")
                                else:
                                    turmas[turmaEscolhida].notas.append(nota)
                                    n[1] = -1
                            
                            except ValueError:
                                print("Nota final invalida.")

                        n[1] = 5

                i = 0
                print("Notas de", turmas[turmaEscolhida].materia, "-", turmaEscolhida)
                print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Nota")
                for discente in discentes:
                    if discente.dre in turmas[turmaEscolhida].alunos:
                        print(f"{discente.dre}  {discente.nome.ljust(20)}  {turmas[turmaEscolhida].notas[i]}")
                        i += 1
            # mostrar todos os discentes de uma turma (alfabético)
            elif n[1] == 6:
                print("Mostrar Alunos da Turma")

                # escolhar turma
                turmaEscolhida = turmaInput()
                
                i = 0
                print("Notas de", turmas[turmaEscolhida].materia, "-", turmaEscolhida)
                print("DRE".ljust(9) + "  " + "Nome".ljust(20) + "  " + "Nota")
                for discente in discentes:
                    if discente.dre in turmas[turmaEscolhida].alunos:
                        print(f"{discente.dre}  {discente.nome.ljust(20)}  {turma[turmaEscolhida][i]}")
                        i += 1

            # mostrar todas as turmas (número de alunos)
            elif n[1] == 7:
                print("Mostrar Turmas")

                # nao esta em ordem
                print("ID  " + "Matéria".ljust(30) + "  " + "Docente".ljust(20))
                for turma in turmas:
                    print(turmas.index(turma), " ", turma)

            # fechar o menu turmas
            elif n[1] == 0:
                print("Saindo do menu turmas...")

    # fechar programa
    elif n[0] == 0:
        print("Saindo do programa...")
        break
    
    # reset
    n = [-1] * 3