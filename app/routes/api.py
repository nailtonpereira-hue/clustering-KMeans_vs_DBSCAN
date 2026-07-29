from flask import Blueprint, jsonify, render_template

from app.services.storage import read_csv
from app.services.config import PCA_GRAFICO

api = Blueprint("api", __name__)


@api.route("/")
def index():
    return render_template("index.html")

@api.route("/dados")
def dados():
    dados = read_csv(PCA_GRAFICO)
    return jsonify(dados)