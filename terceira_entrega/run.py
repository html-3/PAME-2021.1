from app import create_app
from dummy_data import criar_dd


if __name__ == "__main__":
    
    app = create_app()

    criar_dd(app) 

    app.run()