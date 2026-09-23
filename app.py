from flask import Flask, render_template, redirect, url_for, session, request
import os

app = Flask(__name__)

app.secret_key = "chave-simulacao-escolar"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()

        if not nome:
            nome = "Servidor Teste"

        # Dados exclusivamente fictícios para a simulação escolar.
        session["servidor"] = nome

        return redirect(url_for("painel"))

    return render_template("login.html")


@app.route("/entrar", methods=["POST"])
def entrar():
    nome = request.form.get("nome", "").strip()

    if not nome:
        nome = "Servidor Teste"

    # Dados exclusivamente fictícios para a simulação escolar.
    session["servidor"] = nome

    return redirect(url_for("painel"))


@app.route("/painel")
def painel():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "painel.html",
        servidor=session["servidor"]
    )


@app.route("/documentos")
def documentos():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "documentos.html",
        servidor=session["servidor"]
    )


@app.route("/financeiro")
def financeiro():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "financeiro.html",
        servidor=session["servidor"]
    )


@app.route("/gerar-boleto")
def gerar_boleto():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "gerar_boleto.html",
        servidor=session["servidor"]
    )


@app.route("/boleto")
def boleto():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "boleto.html",
        servidor=session["servidor"]
    )


@app.route("/pagamento")
def pagamento():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "pagamento.html",
        servidor=session["servidor"]
    )


@app.route("/revelacao")
def revelacao():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "revelacao.html",
        servidor=session["servidor"]
    )


@app.route("/video")
def video():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "video.html",
        servidor=session["servidor"]
    )


@app.route("/quiz")
def quiz():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "quiz.html",
        servidor=session["servidor"]
    )


@app.route("/perfil")
def perfil():
    if "servidor" not in session:
        return redirect(url_for("login"))

    return render_template(
        "perfil.html",
        servidor=session["servidor"]
    )


@app.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )