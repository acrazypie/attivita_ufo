from models import db, Admin
from flask import flash


def create_admin_account(username, password):

    existing = Admin.query.filter_by(username=username).first()

    if not existing:
        new_admin = Admin()
        new_admin.username = username
        new_admin.set_password(password)
        db.session.add(new_admin)
        db.session.commit()
