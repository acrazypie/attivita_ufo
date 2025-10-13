import os
from flask import Flask
from app import create_app
from config import config


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


if __name__ == "__main__":
    create_app(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=config.DEBUG)
