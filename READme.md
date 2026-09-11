### 1 Liste pelo menos 4 problemas arquiteturais que você encontrou no código inicial e explique
### por que cada um viola o padrão MVC.
1* Criação de classes no app.py, enquanto deveria estar em models.

2* Falta de registro dos blueprints no app.py

3* No routes.py, o app estava sendo importado de app, o que não é necessário, e não havia o import do blueprint. A rota 
de servicos também usava a rota de maneira errada, sem citar o blueprint.


4* Mistura dos templates. No início, todos os templates estavam em um só lugar, enquanto, na verdadem, deveriam estar separados
em pastas como templates/auth e templates/servicos

### 2 Onde ficou a camada Model no seu projeto? Onde ficaram os Controllers? Cite um trecho de cada.

A camada model permanecel no diretório raiz do projeto - base - . os Controlers agora se encontram na parte das rotas
dos blueprints. Exemplos:

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for u in models.usuarios:
            if u["nome"] == request.form["nome"] and u["senha"] == request.form["senha"]:
                session["usuario"] = u["nome"]
                return redirect(url_for("servicos.index"))
        return render_template("auth/login.html", erro="Usuário ou senha inválidos")
    return render_template("auth/login.html")

@servicos_bp.route("/servicos")
def listar_servicos():
    return render_template("servicos./index.html", servicos=models.servicos)


### 3 Por que o url_for e os endpoints precisaram ser ajustados durante a refatoração? Cite um exemplo de mudança que você fez.

Poreque precisamos referenciar que aquelas rotas pertencem a um blueprint, e não a uma aplicação tradicional.

exemplo encontrado em login.html dentro dos templates de auth:

{{url_for('login')}}
{{url_for('auth.login')}}

Adicionamos o nome do blueprint antes da rota para fazer a referência de que a rota login é parte do blueprint