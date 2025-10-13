import csv, os
from datetime import datetime
from app.models.models import db, Admin


def create_admin_account(username, password):

    existing = Admin.query.filter_by(username=username).first()

    if not existing:
        new_admin = Admin()
        new_admin.username = username
        new_admin.set_password(password)
        db.session.add(new_admin)
        db.session.commit()


def export_user_csv(user):
    filename = f"export_{user.username}_{datetime.now().strftime('%Y%m%d')}.csv"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Data Presenza"])
        for p in user.presenze:
            writer.writerow([p.data.strftime("%d/%m/%Y")])
    return filepath


def export_all_users(users):
    filename = f"export_all_users_{datetime.now().strftime('%Y%m%d')}.csv"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nome", "Cognome", "Username", "Data Presenza"])

        for user in users:
            for p in user.presenze:
                writer.writerow(
                    [
                        user.nome,
                        user.cognome,
                        user.username,
                        p.data.strftime("%d/%m/%Y"),
                    ]
                )

    return filepath
