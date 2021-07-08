from app.extensions import db
from datetime import datetime
from app.medicos.model import Medico
from app.pacientes.model import Paciente
from app.consultas.model import Consulta
from app.exames.model import Exame
from app.receitas.model import Receita

def criar_dd(app):
    with app.app_context():
        db.create_all()

    db.session.commit()

    if not Medico.query.filter_by(id="0").first():
        olivia = Medico(nome="Olivia Gonzalvez",
                        esp="Obstetra"
                       )
        gustavo = Medico(nome="Gustavo Martins",
                         esp="Ginecologista",
                         cel="(21)9999-9999",
                         email="martins.gus@gmail.com"
                       )

        db.session.add(olivia)
        db.session.add(gustavo)
        db.session.commit()

    if not Paciente.query.filter_by(id="0").first():
        maria = Paciente(nome="Maria Rocha",
                         cpf="111.111.111-11",
                         cel="(21)9999-9991",
                         email="maria_rocha@gmail.com"
                       )
        luiza = Paciente(nome="Luiza Silva",
                         cpf="222.222.222-22",
                         cel="(21)9999-9992",
                         email="luiza2000@gmail.com"
                       )

        db.session.add(maria)
        db.session.add(luiza)
        db.session.commit()

    if not Consulta.query.filter_by(id="0").first():
        db.session.add(Consulta(horario=datetime(2021,7,10,16,30),
                                paciente=maria,
                                medico=gustavo
                      ))
        db.session.add(Consulta(horario=datetime(2021,7,9,15,30),
                                paciente=luiza,
                                medico=olivia
                      ))

        db.session.commit()

    if not Receita.query.filter_by(id="0").first():
        db.session.add(Receita(data=datetime(2021,7,10),
                               cont="1 paracetamol, ultrassom",
                               paciente=maria,
                               medico=gustavo
                      ))
        db.session.add(Receita(data=datetime(2021,7,9),
                               cont="1 anticoncepcional",
                               paciente=luiza,
                               medico=olivia
                      ))

        db.session.commit()

    if not Exame.query.filter_by(id="0").first():
        db.session.add(Exame(horario=datetime(2021,7,10,15,30),
                               tipo="Ultrassom",
                               paciente=maria,
                               medico=gustavo
                      ))
        db.session.add(Exame(horario=datetime(2021,7,11,16,30),
                               tipo="Rotina",
                               paciente=luiza,
                               medico=olivia
                      ))

        db.session.commit()

    db.session.commit()
