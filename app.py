# app.py — Oficina de Conserto (versão inicial)
from flask import Flask
app = Flask(__name__)

app.secret_key = "oficina-secreta"

from blueprints.servicos import servicos_bp
from blueprints.auth import auth_bp

app.register_blueprint(servicos_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)