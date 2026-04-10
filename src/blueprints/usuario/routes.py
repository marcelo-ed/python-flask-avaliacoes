from flask import Blueprint, request, jsonify

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Criar usuário
@usuarios_bp.route('/', methods=['POST'])
def criar_usuario():
    return jsonify({"msg": "Usuário criado"})

# Listar usuários
@usuarios_bp.route('/', methods=['GET'])
def listar_usuarios():
    return jsonify({"usuarios": []})

# Buscar usuário por ID
@usuarios_bp.route('/<int:id>', methods=['GET'])
def buscar_usuario(id):
    return jsonify({"id": id})

# Atualizar
@usuarios_bp.route('/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    return jsonify({"msg": f"Usuário {id} atualizado"})

# Deletar
@usuarios_bp.route('/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    return jsonify({"msg": f"Usuário {id} deletado"})