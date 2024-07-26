from flask.cli import FlaskGroup
from NikaidoShinku_market import create_app

def create_app_cli():
    return create_app()

cli = FlaskGroup(create_app=create_app_cli)

if __name__ == '__main__':
    cli()