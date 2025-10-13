from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import db, Admin, User, Presenza
from utils.export import export_user_csv, export_all_users
from flask import send_file

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Credenziali errate ⚠️", "danger")
            return render_template("admin_login.html")

    return render_template("admin_login.html")


@admin_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout effettuato ✅", "success")
    return redirect(url_for("admin.login"))


@admin_bp.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user = None
    users = User.query.all()
    if request.method == "POST":
        username = request.form.get("username")
        user = User.query.filter_by(username=username).first()
    return render_template("admin_dashboard.html", users=users, user=user)


@admin_bp.route("/user/<username>")
@login_required
def user_detail(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template("user_detail.html", error="Utente non trovato")
    presenze = (
        Presenza.query.filter_by(user_id=user.id).order_by(Presenza.data.desc()).all()
    )
    return render_template("user_detail.html", user=user, presenze=presenze)


@admin_bp.route("/user/<username>/export")
@login_required
def export_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return "Utente non trovato", 404
    csv_path = export_user_csv(user)
    return send_file(csv_path, as_attachment=True)


@admin_bp.route("/export/users")
@login_required
def export_all():
    users = User.query.all()
    if not users:
        return "Nessun utente regitrato", 404
    csv_path = export_all_users(users)
    return send_file(csv_path, as_attachment=True)
