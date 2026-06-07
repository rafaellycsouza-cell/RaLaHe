from flask import Blueprint, request, jsonify, render_template
import mysql.connector

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    """Renderiza a estrutura unificada (SPA) contendo todas as novas regras e lojas."""
    return render_template('base.html')

@main_blueprint.route('/api/atualizar-bairro', methods=['POST'])
def atualizar_bairro():
    """Mapeia e sincroniza assincronamente a rota e o bairro do cliente no banco de dados."""
    dados = request.get_json()
    if not dados:
        return jsonify({"success": False, "message": "Dados inválidos"}), 400
        
    username = dados.get('username')
    bairro = dados.get('bairro')

    if not username or not bairro:
        return jsonify({"success": False, "message": "Campos vazios"}), 400

    conexao = None
    cursor = None
    try:
        from config import Config
        conexao = mysql.connector.connect(**Config.get_db_credentials())
        cursor = conexao.cursor()

        sql = "UPDATE cliente SET bairro = %s WHERE username = %s"
        cursor.execute(sql, (bairro.lower().strip(), username.lower().strip()))
        conexao.commit()

        return jsonify({"success": True, "message": "Dados salvos no MySQL."}), 200
    except Exception as e:
        print(f"Erro operacional no MySQL: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conexao: conexao.close()