# app.py — Quitanda da Esquina (versão inicial)
from flask import Flask, render_template, request, redirect, url_for, session
import models
from blueprints.auth import auth_bp
from blueprints.produtos import produtos_bp

app = Flask(__name__)
app.secret_key = "quitanda-secreta"
app.register_blueprint(auth_bp)
app.register_blueprint(produtos_bp)

if __name__ == "__main__":
    app.run(debug=True)