from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify

pedido_blueprint = Blueprint('pedido', __name__)

@pedido_blueprint.route('/salvar_endereco_sessao', methods=['POST'])
def salvar_endereco_sessao():
    """Recebe as coordenadas reais e o texto do Google Maps e salva na Session."""
    dados = request.get_json()
    if not dados or 'endereco' not in dados or 'lat' not in dados or 'lng' not in dados:
        return jsonify({"status": "erro", "mensagem": "Dados de localização incompletos ou inválidos"}), 400
        
    session['endereco_entrega'] = {
        'texto': dados['endereco'],
        'lat': float(dados['lat']),
        'lng': float(dados['lng'])
    }
    return jsonify({"status": "sucesso", "mensagem": "Endereço registrado com sucesso!"})

@pedido_blueprint.route('/finalizar_pedido', methods=['POST'])
def finalizar_pedido():
    """Valida estritamente se o endereço foi selecionado antes de fechar a compra."""
    if not session.get('endereco_entrega'):
        flash("Erro: Você não selecionou um endereço de entrega! Por favor, utilize o mapa abaixo para definir um local real antes de continuar.", "danger")
        return redirect(url_for('pedido.exibir_entrega'))
        
    # Se passou na validação, pode processar no Banco de Dados e mandar para o rastreio
    return redirect(url_for('pedido.exibir_status'))

@pedido_blueprint.route('/delivery/entrega')
def exibir_entrega():
    """Página de seleção de endereço com design temático."""
    return render_template('delivery/entrega.html')

@pedido_blueprint.route('/delivery/status')
def exibir_status():
    """Página de monitoramento do motoboy."""
    endereco = session.get('endereco_entrega')
    if not endereco:
        flash("Selecione um endereço de entrega primeiro.", "warning")
        return redirect(url_for('pedido.exibir_entrega'))
    return render_template('delivery/status.html', endereco=endereco)