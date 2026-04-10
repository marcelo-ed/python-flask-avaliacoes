from flask import Blueprint, jsonify

itens_bp = Blueprint('itens', __name__, url_prefix='/itens')

@itens_bp.route('/', methods=['GET'])
def listar_itens():
    return jsonify({"itens": []})

@itens_bp.route('/<int:id>', methods=['GET'])
def detalhe_item(id):
    return jsonify({"item": id})

@itens_bp.route('/', methods=['POST'])
def cadastrar_itens(): #adicionar um parametro para cadastrar o item
    return jsonify({"msg": "Item cadastrado"})

    