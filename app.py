import os
from flask import Flask
from flask_login import LoginManager
from pathlib import Path
from models import db, Admin
from utils.create_admin import create_admin_account

# admin di test
admin_username = "admin"
admin_password = "admin123"


def create_app():
    app = Flask(__name__)
    app.secret_key = "qualcosa_di_casuale"  # chiave di sicurezza

    BASE_DIR = Path(__file__).resolve().parent
    DB_DIR = BASE_DIR / "db"
    DB_DIR.mkdir(exist_ok=True)
    db_path = DB_DIR / "attivita_ufo.db"

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    setattr(login_manager, "login_view", "admin.login")

    @login_manager.user_loader
    def load_user(admin_id):
        return Admin.query.get(int(admin_id))

    from routes import main_bp, admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    with app.app_context():
        db.create_all()
        create_admin_account(admin_username, admin_password)

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
