from app.dao.db_connection import DBConnection
from app.models.produto import Produto

class ProdutoDAO:
    def listar_todos(self):
        # Lista padrão caso o MySQL esteja offline (Evita o erro InterfaceError)
        produtos_fallback = [
            Produto(1, 'Classic Chicken Shawarma', 'Frango grelhado marinado em especiarias árabes, pasta de alho artesanal e picles no pão sírio.', 28.00, 'https://images.unsplash.com/photo-1644243533276-8051772b1a8d?auto=format&fit=crop&w=400&q=80', 'Shawarmas'),
            Produto(2, 'Prato Beef Shawarma', 'Tiras de carne bovina, arroz com lentilha, homus, salada fatuche e pão sírio quentinho.', 42.00, 'https://images.unsplash.com/photo-1541518763669-27fef04b14ea?auto=format&fit=crop&w=400&q=80', 'Combos'),
            Produto(3, 'Porção de Falafel (6 unid.)', 'Bolinhos de grão-de-bico fritos na hora, crocantes por fora e macios por dentro. Acompanha hortelã e molho tarine.', 22.00, 'https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=400&q=80', 'Mezze'),
            Produto(4, 'Ninho de Nozes (Doce Árabe)', 'Delicada massa folhada recheada com nozes selecionadas e banhada em calda de especiarias.', 12.00, 'https://images.unsplash.com/photo-1519676867240-f03562e64548?auto=format&fit=crop&w=400&q=80', 'Doces')
        ]
        
        try:
            conexao = DBConnection.get_connection()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM produtos")
            resultados = cursor.fetchall()
            cursor.close()
            conexao.close()
            
            if resultados:
                produtos = []
                for r in resultados:
                    produtos.append(Produto(r['id'], r['nome'], r['descricao'], r['preco'], r['imagem_url'], r['categoria']))
                return produtos
            return produtos_fallback
        except Exception:
            # Se o banco estiver desligado, ele usa os dados locais de segurança automaticamente!
            return produtos_fallback