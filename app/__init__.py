from flask import Flask
from app.config import Config
from app.extensions import db, migrate

# Import semua model di sini agar Flask-Migrate bisa mendeteksi tabelnya
from app.models.user_model import User
from app.models.task_model import Task

from app.routes.user_routes import user_blueprint
from app.routes.task_routes import task_blueprint



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_blueprint, url_prefix = "/api")
    app.register_blueprint(task_blueprint, url_prefix = "/api")

    return app