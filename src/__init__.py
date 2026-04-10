from flask import Flask
from blueprints.usuario import usuarios_bp
from blueprints.itens import itens_bp
from blueprints.paginas import paginas_bp

app = Flask(__name__)

# Registrando rotas
app.register_blueprint(usuarios_bp)
app.register_blueprint(itens_bp)
app.register_blueprint(paginas_bp)

if __name__ == '__main__':
    app.run(debug=True)