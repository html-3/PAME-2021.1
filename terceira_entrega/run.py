from app import create_app
from dummy_data import criar_dd


app = create_app()

criar_dd()

if __name__ == "__main__":
    
    app.run()