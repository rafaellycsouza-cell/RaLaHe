import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta_ralahe_123'
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''  # Deixe vazio se usar XAMPP, ou coloque sua senha do MySQL
    DB_NAME = 'delivery_arabe'