import time
from app.dao.db_connection import DBConnection

class ClienteDAO:
    @staticmethod
    def cadastrar(username, senha, email, telefone, endereco, bairro):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Gerando um CPF fictício estável de 11 números para preencher a PK do banco
        id_cpf = str(int(time.time()))[:11].zfill(11)
        
        # Como o base.html usa o nome completo e o username de forma síncrona
        nome_completo = username 

        try:
            sql = """
                INSERT INTO cliente (id_cpf, username, nome_completo, email, senha, telefone, endereco, bairro)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (id_cpf, username, nome_completo, email, senha, telefone, endereco, bairro)
            cursor.execute(sql, valores)
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar cliente no MySQL: {e}")
            return False
        finally:
            cursor.close()

    @staticmethod
    def buscar_por_username(username):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT * FROM cliente WHERE LOWER(username) = %s"
            cursor.execute(sql, (username.lower(),))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar cliente: {e}")
            return None
        finally:
            cursor.close()