# run.py

from flask import Flask, render_template
from config import Config

# =========================
# CRIAÇÃO DO APP
# =========================

app = Flask(__name__)

# Carrega as configurações do config.py
app.config.from_object(Config)


# =========================
# ROTA PRINCIPAL
# =========================

@app.route('/')
def home():
    return f'''
    <h1>{Config.NOME_EMPRESA}</h1>

    <h2>Bem-vindo ao Delivery Árabe!</h2>

    <p><b>Telefone:</b> {Config.TELEFONE}</p>

    <p><b>Tempo Médio:</b> {Config.TEMPO_MEDIO_ENTREGA}</p>

    <p><b>Taxa de Entrega:</b> R$ {Config.TAXA_ENTREGA}</p>

    <h3>Pratos Populares:</h3>

    <ul>
        <li>Esfiha</li>
        <li>Kibe</li>
        <li>Shawarma</li>
        <li>Falafel</li>
        <li>Homus</li>
        <li>Tabule</li>
    </ul>

    <h3>Formas de Pagamento:</h3>

    <ul>
        <li>Pix</li>
        <li>Cartão de Crédito</li>
        <li>Cartão de Débito</li>
        <li>Dinheiro</li>
    </ul>
    '''


# =========================
# EXECUTAR O SERVIDOR
# =========================

if __name__ == '__main__':
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )