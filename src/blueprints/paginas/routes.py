from flask import Blueprint, render_template

paginas_bp = Blueprint('paginas', __name__)

# 🏠 Home
@paginas_bp.route('/')
def home():
    return render_template('home.html')


# 🔐 Login
@paginas_bp.route('/login')
def login():
    return render_template('login.html')


# 📝 Registrar usuário
@paginas_bp.route('/registrar')
def registrar():
    return render_template('registrar.html')


# 🎬📚 Catálogo de itens
@paginas_bp.route('/itens')
def catalogo_itens():
    itens = Item.query.all()
    return render_template('catalogo.html')


# 📄 Página de um item (dinâmica)
@paginas_bp.route('/item/<int:id>')
def pagina_item(id):
    item = Item.query.get(id)
    return render_template('item.html', id=id)


# ➕ Registrar novo item
@paginas_bp.route('/novo-item')
def novo_item():
    return render_template('novo_item.html')