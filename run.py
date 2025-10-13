from flask import Flask
from app import create_app
from config import config


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


if __name__ == "__main__":
    create_app(app)
    app.run(debug=config.DEBUG)
