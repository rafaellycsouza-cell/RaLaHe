import mysql.connector
from flask import current_app
import os

class DBConnection:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME']
        )

    @staticmethod
    def init_db(app):
        conn = mysql.connector.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD']
        )
        cursor = conn.cursor()

        db_name = app.config['DB_NAME']
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
        cursor.execute(f"USE `{db_name}`")

        sql_path = os.path.join(os.path.dirname(__file__), '..', '..', 'banco de dados', 'scriptpronto.sql')
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql = f.read()

        # Remove CREATE DATABASE and USE statements since we already handled them
        lines = [line for line in sql.splitlines()
                 if not line.strip().upper().startswith('CREATE DATABASE')
                 and not line.strip().upper().startswith('USE ')]
        sql = '\n'.join(lines)

        for statement in sql.split(';'):
            statement = statement.strip()
            if statement:
                try:
                    cursor.execute(statement)
                except mysql.connector.Error:
                    pass  # Table already exists

        conn.commit()
        cursor.close()
        conn.close()
