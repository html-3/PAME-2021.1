from app.extensions import db
from datetime import datetime
from app.medicos.model import Medico
from app.pacientes.model import Paciente
from app.consultas.model import Consulta
from app.exames.model import Exame
from app.receitas.model import Receita

# funcao para criar a database e os dados ficticios
def criar_db(app):

    # todos os comandos dessa funcao estao identados 
    # para poderem usar a variavel app, local aa funcao create_app()
    # pelo contrario ocorreria um erro de contexto
    with app.app_context():

        # criar e comitar as databases (vazias)
        db.create_all()
        db.session.commit()

        # conferir se a base de dados nao existe

        # perceba que os medicos e os pacientes foram instanciados,
        # isto ocorre para poderem ser inseridos como argumentos
        # nas consultas, exames e receitas

        if not Medico.query.filter_by(id="1").first():
            olivia = Medico(nome="Olivia Gonzalvez",
                            esp="Obstetra"
                        )
            gustavo = Medico(nome="Gustavo Martins",
                            esp="Ginecologista",
                            cel="(21) 9999-9993",
                            email="martins.gus@gmail.com"
                        )
            jonas = Medico(nome="Jonas Johnson",
                           esp="Pediatra",
                           email="jojo1970@gmail.com"
                        )

            db.session.add(olivia)
            db.session.add(gustavo)
            db.session.add(jonas)
            db.session.commit()

        if not Paciente.query.filter_by(id="1").first():
            maria = Paciente(nome="Maria Rocha",
                            cpf="111.111.111-11",
                            cel="(21)9999-9991",
                            email="maria_rocha@gmail.com",
                            plano_saude="Golden Cross Premium"
                        )
            luiza = Paciente(nome="Luiza Silva",
                            cpf="222.222.222-22",
                            cel="(21)9999-9992",
                            email="luiza2000@gmail.com",
                            plano_saude="Unimed Alpha"
                        )

            db.session.add(maria)
            db.session.add(luiza)
            db.session.commit()

        if not Consulta.query.filter_by(id="1").first():
            db.session.add(Consulta(horario=datetime(2021,7,10,16,30),
                                    paciente=maria,
                                    medico=gustavo
                        ))
            db.session.add(Consulta(horario=datetime(2021,6,15,16,30),
                                    paciente=maria,
                                    medico=jonas
                        ))
            db.session.add(Consulta(horario=datetime(2021,7,9,15,30),
                                    paciente=luiza,
                                    medico=olivia
                        ))

            db.session.commit()

        if not Receita.query.filter_by(id="1").first():
            db.session.add(Receita(data=datetime(2021,7,10),
                                cont="1 paracetamol, ultrassomp",
                                paciente=maria,
                                medico=gustavo
                        ))
            db.session.add(Receita(data=datetime(2021,6,15),
                                cont="1 apevitim",
                                paciente=maria,
                                medico=jonas
                        ))
            db.session.add(Receita(data=datetime(2021,7,9),
                                cont="1 anticoncepcional",
                                paciente=luiza,
                                medico=olivia
                        ))

            db.session.commit()

        if not Exame.query.filter_by(id="1").first():
            db.session.add(Exame(horario=datetime(2021,7,10,15,30),
                                tipo="Ultrassom",
                                paciente=maria
                        ))
            db.session.add(Exame(horario=datetime(2021,5,11,16,30),
                                tipo="Rotina",
                                paciente=luiza
                        ))
            db.session.add(Exame(horario=datetime(2021,6,11,16,30),
                                tipo="Rotina",
                                paciente=luiza
                        ))
            db.session.add(Exame(horario=datetime(2021,7,11,16,30),
                                tipo="Rotina",
                                paciente=luiza
                        ))

            db.session.commit()

        # um commit adicional, pelas duvidas
        db.session.commit()
