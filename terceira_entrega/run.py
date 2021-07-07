from app import create_app
from dummy_data import criar_dd

if __name__ == "__main__":
    criar_dd()

    app = create_app()
    app.run()