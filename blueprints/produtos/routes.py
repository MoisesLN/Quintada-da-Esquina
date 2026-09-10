from flask import render_template, request, session
import models
from . import produtos_bp

@produtos_bp.route("/produtos/<int:produto_id>")
def ver_produto(produto_id):
    produto = models.buscar_produto(produto_id)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template('ver-produto.html', produto=produto, user=session.get('usuario', None))

@produtos_bp.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = [p for p in models.produtos if q.lower() in p["nome"].lower()]
    else:
        lista = models.produtos
    return render_template("index.html", produtos=lista, q=q, user=session.get('usuario', None),
                           categorias=models.todas_categorias())