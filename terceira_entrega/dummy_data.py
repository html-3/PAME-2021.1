from app.extensions import db
from datetime import datetime
from app.consultas.model import Consulta
from app.exames.model import Exame
from app.medicos.model import Medico
from app.pacientes.model import Paciente
from app.receitas.model import Receita

def criar_dd():

    db.create_all()

    db.session.commit()

criar_dd()