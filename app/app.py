from flask import Flask
from app.routes.pages import pages

app = Flask(__name__)

app.register_blueprint(pages)



if __name__ == "__main__":
    app.run(debug=True)
