# Mapa Entidade Relacional
Basicamente a única relação trata sobre os funcionários e as máquinas, qual é do tipo *many-to-many*. Fora disso, são tabelas normais com atributos simples.
## Funcionários
- ID: Chave principal da tabela
- Nome: Nome do funcionário
- Email: Email do funcionário, deve ser único pois serve de login
- Senha Hash: Senha *hashed* da original, tem uma forma *default* pois o cadastro é feito pelos administradores
- Cargo: Cargo do funcionário dentro da empresa
- ADM: Determina se o funcionário é um moderador ou não, possui capacidades extra
 
## Máquina
- ID: Chave principal da tabela
- Tipo: Tipo de máquina (Esteira, Bomba, Empacotadora, etc.)
- Modelo: Modelo ou versão da máquina
- Implementação: Dia de introdução da máquina a fábrica, questões de manutenção
 
## Temperatura
- ID: Chave principal da tabela
- Horário: Instante no qual as medidas foram feitas
- Temperatura 1: Temperatura da máquina 1
- Temperatura 2: Temperatura da máquina 2
- Temperatura 3: Temperatura da máquina 3
- Temperatura 4: Temperatura da máquina 4
- Temperatura 5: Temperatura da máquina 5
 
## Peso
- ID: Chave principal da tabela
- Bolsa ID: ID da bolsa que foi pesada
- Peso Kg: Peso da bolsa pesada
 
## Association table
- Funcionario ID: ID do funcionário
- Máquina ID: ID da máquina
**OBS:** Permite a relação *many-to-many*
 
# Rotas
## Funcionários
- `/login`
   - Função: Login de usuários
   - Métodos: GET
   - Acesso: Todos
- `/funcionarios`
   - Função: Ver todos os usuários e adicionar mais
   - Métodos: GET e POST
   - Acesso: ADM
- `/funcionario/<int:id_escolhido>`
   - Função: Ver, editar ou deletar um usuário
   - Métodos: GET, PATCH e DELETE
   - Acesso: ADM e usuário correspondente
## Máquina
- `/maquinas`
   - Função: Ver todas as máquinas e adicionar mais
   - Métodos: GET e POST (apenas ADM)
   - Acesso: ADM (todas as máquinas) e usuários (suas máquinas)
- `/maquina/<int:id_escolhido>`
   - Função: Ver, editar ou deletar uma máquina
   - Métodos: GET, PATCH e DELETE
   - Acesso: ADM e usuário correspondente
## Registro
- `/temperaturas`
   - Função: Ver todas as temperaturas registradas e adicionar mais
   - Métodos: GET e POST (apenas ADM)
   - Acesso: ADM (ambos) e usuários (apenas GET)
- `/temperatura/<int:id_escolhido>`
   - Função: Ver, editar ou deletar uma temperatura registrada
   - Métodos: GET, PATCH e DELETE
   - Acesso: ADM
- `/pesos`
   - Função: Ver todos os pesos registrados e adicionar mais
   - Métodos: GET e POST (apenas ADM)
   - Acesso: ADM (ambos) e usuários (apenas GET)
- `/peso/<int:id_escolhido>`
   - Função: Ver, editar ou deletar um pesos registrado
   - Métodos: GET, PATCH e DELETE
   - Acesso: ADM

# Quinta Entrega

Roberto possui uma indústria de farinha de milho de muito sucesso, que conta com uma infraestrutura de qualidade, com diversas linhas de produção automatizadas para uma produção em escala, além de um centro de distribuição para que seu produto chegue seguro aos seus clientes.

Para a organização de todos esses dados, ele também solicitou o projeto de um banco de dados para armazenar as leituras diárias e um sistema web de gerenciamento. Nele, todos os funcionários poderão se cadastrar, logar e terão acesso aos dados dos motores que eles trabalham diretamente. Cada motor terá uma lista de funcionários cadastrados que podem visualizar os seus dados e todo funcionário da empresa só poderá visualizar os dados de um motor em que ele possui acesso.
***