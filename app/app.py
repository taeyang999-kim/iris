import os
from flask import Flask
from app.routes.main_routes import bp

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # C:\iris

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static")  # 있으면 같이 추천
    )

    app.register_blueprint(bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)