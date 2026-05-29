class Pedido:
    def __init__(self, id, codigo, status, total, data_criacao):
        self.id = id
        self.codigo = codigo       # Ex: #RLH-9871
        self.status = status       # Confirmado, Preparando, A caminho, Entregue
        self.total = total
        self.data_criacao = data_criacao