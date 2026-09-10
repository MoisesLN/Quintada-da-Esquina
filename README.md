# Prova de Flask

Objetivo: Listar os problemas no README, depois resolvê-los <br>


Problemas:

- Blueprint produtos não utilizada
`produtos_bp = Blueprint("produtos", __name__, template_folder="templates")`

- classe Produto na camada Controller
```python
# app.py
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
```

- Falta link para login no header
```html
<a href="{{ url_for('index') }}">Início</a>
<a href="{{ url_for('logout') }}">Sair</a>
```

- Redirecionamento para página inexistente no login
`return redirect(url_for("painel"))`

- Rotas de Produtos fora da blueprint

- Rota /categorias não utilizada no aplicativo

- HTML retornado diretamente no python
```python
return f"""
    <h2>{produto['nome']}</h2>
    <p>Categoria: {produto['categoria']}</p>
    <p>Preço: R$ {produto['preco']} por {produto['unidade']}</p>
    <a href='/'>Voltar para a quitanda</a>
    """
```

## Defesa escrita (README.md)
Responda com suas palavras e citando trechos do seu código ou do código inicial:
1. Liste pelo menos 4 problemas arquiteturais que você encontrou no código inicial e
explique por que cada um viola o padrão MVC.
Primeiramente a classe Produto no app.py; Como sabemos, o app.py é da camada Controller, e Produto seria na camada models, não Controller. <br>
Segundo, uma url para a página 'painel' que não existe. Essa página não existe no View. <br>
Terceiro, o HTML sendo retornado no python. HTML é da camada View, não Controller. <br>
Quarto, todos os endpoints estavam no arquivo app.py, inclusive de Produto que tinha uma Blueprint inutilizada.  <br>

2. Onde ficou a camada Model no seu projeto? Onde ficaram os Controllers? Cite um trecho de
cada.
o Model ficou no arquivo models.py, incluindo dados.
```python
usuarios = [
    {"id": 1, "nome": "admin", "senha": "1234"},
]

```
O controller ficou organizado nas blueprints/{NOME}/routes.py, como por exemplo a rota de logout em blueprints/auth/routes.py
```python
@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("produtos.index"))
```

3. Por que o url_for e os endpoints precisaram ser ajustados durante a refatoração? Cite
um exemplo de mudança que você fez.
Pois, ao botar uma função rota 'index' em uma blueprint 'produtos', para acessar ela temos que utilizar 'produtos.index'. Como exemplo, temos na página index.html que acessava ver_produto diretamente, e ao colocar essa função na bp produtos, teve que ser mudada para:
```html
<a href="{{ url_for('produtos.ver_produto', produto_id=p['id']) }}">Ver detalhes</a>
```