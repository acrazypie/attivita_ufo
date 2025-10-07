from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import Admin

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
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

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
