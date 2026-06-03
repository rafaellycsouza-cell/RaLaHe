from flask import Flask

def create_app():
    # 1. Inicializa o objeto do Flask [1, 3]
    app = Flask(__name__)

    # 2. Configurações da aplicação (ex: Secret Key para mensagens flash) [4, 5]
    # Recomenda-se carregar do arquivo config.py da raiz [6]
    app.config.from_object('config')

    # 3. Registro de Blueprints (Controllers) [1, 2]
    # Importa os Blueprints definidos na camada Controller [7]
    from app.controllers.usuario_controller import usuario_bp
    
    # Registra a rota para que o Flask a reconheça [2]
    app.register_blueprint(usuario_bp)

    # Caso existam outros controllers (ex: produto), eles seriam registrados aqui
    # from app.controllers.produto_controller import produto_bp
    # app.register_blueprint(produto_bp)

    return app