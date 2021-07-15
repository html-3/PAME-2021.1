from app import create_app

if __name__ == "__main__":
    app = create_app()

    app.run()

# flask db init
# flask db migrate
# flask db upgrade

"""
Funcionario Test
{
	"nome": "Pedro Rocha",
	"registro": "pedro_rocha1",
	"senha": "senha456",
	"cargo": "Operador de Máquina"
}
Pedro Rocha Pedro Rocha Pedro 
"""