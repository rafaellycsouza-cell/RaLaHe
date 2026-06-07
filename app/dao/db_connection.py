import mysql.connector
from flask import current_app, g

class DBConnection:
    @staticmethod
    def init_db(app):
        """ Inicializa os ganchos do Flask para limpar conexões pendentes no encerramento da requisição """
        @app.teardown_appcontext
        def close_db(error):
            db = g.pop('db_conn', None)
            if db is not None:
                db.close()

    @staticmethod
    def get_connection():
        """ Recupera a conexão MySQL ativa no contexto da requisição atual ou abre uma nova caso não exista """
        if 'db_conn' not in g:
            config = current_app.config
            g.db_conn = mysql.connector.connect(
                host=config.get('DB_HOST', 'localhost'),
                user=config.get('DB_USER', 'root'),
                password=config.get('DB_PASSWORD', ''),
                database=config.get('DB_NAME', 'delivery_arabe')
            )
        return g.db_conn