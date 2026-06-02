from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.controllers.main_controller import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.dao.db_connection import DBConnection
    DBConnection.init_db(app)

    return app