from app.extensions import db

tabela_funcionario_maquina = db.Table(
        'association', 

        db.Column('funcionario', db.Integer, db.ForeignKey('funcionario.id')),
        db.Column('maquina', db.Integer, db.ForeignKey('maquina.id'))

        )