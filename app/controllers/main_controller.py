from flask import Blueprint, render_template
from app.dao.produto_dao import ProdutoDAO

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    dao = ProdutoDAO()
    cardapio = dao.listar_todos()
    return render_template('delivery/home.html', cardapio=cardapio)