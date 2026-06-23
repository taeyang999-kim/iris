from flask import Flask
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates")
    )

    from app.routes.main_routes import bp
    app.register_blueprint(bp)

    return app