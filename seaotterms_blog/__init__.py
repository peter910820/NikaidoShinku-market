from flask import Flask

def create_app():
    app = Flask(__name__)

    app.static_folder = 'static'
    app.static_url_path = '/static'

    with app.app_context():
        from . import routes

        app.register_blueprint(routes.routes_bp)

    return app