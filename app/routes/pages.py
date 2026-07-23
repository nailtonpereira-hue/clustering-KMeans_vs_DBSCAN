from flask import Blueprint, render_template
from app.services.storage import read_csv
from app.config import CENARIOS_FILE

pages = Blueprint("pages", __name__)

@pages.route("/teste")
def teste():
	cenarios = read_csv(CENARIOS_FILE)

	print(cenarios)
	return render_template("teste.html", cenarios=cenarios)
