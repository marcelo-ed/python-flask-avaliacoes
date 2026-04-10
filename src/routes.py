from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Usuario, Item, Avaliacao
from extensions import db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(gmail=email, senha=senha).first()

        if usuario:
            session["usuario_id"] = usuario.id_usuario
            return redirect(url_for("main.catalogo"))
        else:
            return "Login inválido"

    return render_template("login.html")


@main.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        email = request.form["email"]
        senha = request.form["senha"]

        novo_usuario = Usuario(
            nome=nome,
            idade=idade,
            gmail=email,
            senha=senha
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("registrar.html")


@main.route("/logout")
def logout():
    session.pop("usuario_id", None)
    return redirect(url_for("main.login"))


@main.route("/catalogo")
def catalogo():
    itens = Item.query.all()
    return render_template("catalogo.html", itens=itens)


@main.route("/item/<int:id>", methods=["GET", "POST"])
def item(id):
    item_obj = Item.query.get(id)

    if not item_obj:
        return "Item não encontrado"

    avaliacoes = Avaliacao.query.filter_by(id_item=id).all()
    usuario_id = session.get("usuario_id")

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "deletar":
            if not usuario_id:
                return redirect(url_for("main.login"))

            Avaliacao.query.filter_by(id_item=id).delete()
            db.session.delete(item_obj)
            db.session.commit()

            return redirect(url_for("main.catalogo"))

        elif acao == "avaliar":
            if not usuario_id:
                return redirect(url_for("main.login"))

            try:
                nota = float(request.form["nota"])
            except:
                return "Nota inválida"

            comentario = request.form["comentario"]

            avaliacao_existente = Avaliacao.query.filter_by(
                id_usuario=usuario_id,
                id_item=id
            ).first()

            if avaliacao_existente:
                return "Você já avaliou este item!"

            if nota < 1 or nota > 5:
                return "A nota deve ser entre 1 e 5!"

            nova_avaliacao = Avaliacao(
                id_usuario=usuario_id,
                id_item=id,
                nota=nota,
                comentario=comentario
            )

            db.session.add(nova_avaliacao)
            db.session.commit()

            return redirect(url_for("main.item", id=id))

    return render_template("item.html", item=item_obj, avaliacoes=avaliacoes)


@main.route("/novo_item", methods=["GET", "POST"])
def novo_item():
    if request.method == "POST":
        titulo = request.form["titulo"]
        ano = request.form["ano"]
        tipo = request.form["tipo"]
        descricao = request.form["descricao"]

        novo = Item(
            titulo=titulo,
            ano=ano,
            tipo=tipo,
            descricao=descricao
        )

        db.session.add(novo)
        db.session.commit()

        return redirect(url_for("main.catalogo"))

    return render_template("novo_item.html")


@main.route("/editar_item/<int:id>", methods=["GET", "POST"])
def editar_item(id):
    item = Item.query.get(id)

    if not item:
        return "Item não encontrado"

    if request.method == "POST":
        item.titulo = request.form["titulo"]
        item.ano = request.form["ano"]
        item.tipo = request.form["tipo"]
        item.descricao = request.form["descricao"]

        db.session.commit()
        return redirect(url_for("main.item", id=id))

    return render_template("editar_item.html", item=item)
