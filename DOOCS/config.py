# config.py

class Config:
    
    # =========================
    # CONFIGURAÇÕES DO FLASK
    # =========================
    
    SECRET_KEY = 'delivery_arabe_2026'
    DEBUG = True

    HOST = '127.0.0.1'
    PORT = 5000


    # =========================
    # BANCO DE DADOS
    # =========================
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/delivery_arabe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # =========================
    # INFORMAÇÕES DO DELIVERY
    # =========================
    
    NOME_EMPRESA = 'Sultão Delivery Árabe'

    TELEFONE = '(47) 99999-9999'

    EMAIL_SUPORTE = 'suporte@sultaodelivery.com'

    ENDERECO = 'Rua das Especiarias, 150 - Joinville/SC'


    # =========================
    # CONFIGURAÇÕES DE PEDIDO
    # =========================
    
    TAXA_ENTREGA = 8.50

    TEMPO_MEDIO_ENTREGA = '40 minutos'

    PEDIDO_MINIMO = 25.00


    # =========================
    # FORMAS DE PAGAMENTO
    # =========================
    
    PAGAMENTOS_ACEITOS = [
        'Pix',
        'Cartão de Crédito',
        'Cartão de Débito',
        'Dinheiro'
    ]


    # =========================
    # CARDÁPIO ÁRABE
    # =========================
    
    PRATOS_POPULARES = [
        'Esfiha',
        'Kibe',
        'Shawarma',
        'Falafel',
        'Homus',
        'Tabule'
    ]


    # =========================
    # STATUS DOS PEDIDOS
    # =========================
    
    STATUS_PEDIDOS = [
        'Pedido Recebido',
        'Em Preparo',
        'Saiu para Entrega',
        'Entregue'
    ]