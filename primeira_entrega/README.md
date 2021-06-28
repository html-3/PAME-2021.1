# Comandos do git

Fonte: [Básico](https://comandosgit.github.io/#basico)
\
\
Tornar um diretório em um repositório local git 

    git init

Ver o estatus do repositório, qual a *branch* atual e se os arquivos estão *tracked*, *staged*, etc.

    git status

Designar a origem repositório remoto do local

    git remote add origin {link}

##### **OBS:** No lugar de escrever o URL do repositório remoto, escreve-se `origin` no terminal.
\
Adicionar mudanças ao *staging area*

    git add {diretório}

    # diretório inteiro
    git add . 

    # Lista de diretórios
    git add {diretório1}, {diretório2}

Confirmar as mudanças feitas

    git commit -m "{mensagem}"

##### **OBS:** O argumenro `-m` passa uma mensagem que será mostrada no GitHub.
\
Enviar as mudanças feitas de um repositório local para o remoto

    git push origin {branch}

    # Primeiro push deve ser
    git push origin HEAD

Coletar mudancas do repositorio remoto

    git fetch origin

Incorporar as mudancas ao repositorio local

    git pull origin {branch}

##### **OBS:** Equivalente à `git fetch origin` e `git merge {branch}`.
\
Remover um arquivo do Git

    git rm -f {arquivo}

Criar uma nova *branch*

    git branch {branch}

    # Muda para tal branch
    git checkout {branch}

    # Cria e muda para tal branch
    git checkout -b {branch}


# Primeira Entrega
