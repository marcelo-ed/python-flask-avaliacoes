from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    senha = db.Column(db.String(50), nullable=False)
    gmail = db.Column(db.String(50), nullable=False)


class Item(db.Model):
    __tablename__ = 'itens'

    id_item = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer)
    tipo = db.Column(db.Enum('filme', 'livro'))
    descricao = db.Column(db.String(255))


class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'

    id_avaliacao = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    id_item = db.Column(db.Integer, db.ForeignKey('itens.id_item'))
    nota = db.Column(db.Float)
    comentario = db.Column(db.Text)

    usuario = db.relationship("Usuario")
    item = db.relationship("Item")
