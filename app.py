import json
import webbrowser
import os
from flask import Flask, render_template, request, jsonify
from threading import Timer

#Laryssa gosch Dev Sênior Top
app = Flask(__name__)
usuarios_db = {}

def carregar_dados():
    caminho = 'data.json'
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    u = request.json
    nome = u.get('nome')
    senha = u.get('senha')
    if nome in usuarios_db and usuarios_db[nome]['senha'] == senha:
        return jsonify({"status": "erro", "msg": "Usuário já existe!"}), 400
    usuarios_db[nome] = u
    return jsonify({"status": "ok"})

@app.route('/login', methods=['POST'])
def login():
    u = request.json
    user = usuarios_db.get(u['nome'])
    if user and user['senha'] == u['senha']: 
        return jsonify({"status": "ok"})
    return jsonify({"status": "erro"}), 401

@app.route('/dashboard')
def dashboard():
    dados = carregar_dados()
    return render_template('dashboard.html', restaurantes=dados['restaurantes'], cupons=dados['cupons_detalhes'])

@app.route('/carrinho')
def carrinho(): 
    return render_template('carrinho.html')

@app.route('/entrega')
def entrega(): 
    return render_template('entrega.html')

if __name__ == '__main__':
    # CORRIGIDO: Agora o navegador vai abrir na página inicial de login e cadastro!
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    app.run(debug=True, port=5000)