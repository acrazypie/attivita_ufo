from flask import Blueprint, render_template, request, redirect, url_for, send_file
from models import db, User, Presenza
from utils.export import export_user_csv

admin_bp = Blueprint("admin", __name__)


# Login admin (molto semplice, senza JWT)
@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO: autenticazione reale, per ora hardcoded
        if username == "admin" and password == "password":
            return redirect(url_for("admin.dashboard"))
        else:
            return render_template("admin_login.html", error="Credenziali errate")

    return render_template("admin_login.html")


@admin_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    user = None
    if request.method == "POST":
        username = request.form.get("username")
        user = User.query.filter_by(username=username).first()
    return render_template("admin_dashboard.html", user=user)


@admin_bp.route("/user/<username>")
def user_detail(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template("user_detail.html", error="Utente non trovato")
    presenze = (
        Presenza.query.filter_by(user_id=user.id).order_by(Presenza.data.desc()).all()
    )
    return render_template("user_detail.html", user=user, presenze=presenze)


@admin_bp.route("/user/<username>/export")
def export_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return "Utente non trovato", 404

    csv_path = export_user_csv(user)
    return send_file(csv_path, as_attachment=True)
