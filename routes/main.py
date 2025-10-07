from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, User, Presenza
from datetime import date

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        scuola = request.form.get("scuola")
        classe = request.form.get("classe")
        username = request.form.get("username")

        if not username:
            return render_template("register.html", error="Username obbligatorio")

        if User.query.filter_by(username=username).first():
            return render_template("register.html", error="Username già registrato")

        user = User()
        user.nome = nome
        user.cognome = cognome
        user.scuola = scuola
        user.classe = classe
        user.username = username

        db.session.add(user)
        db.session.commit()

        # segna presenza automatica
        presenza = Presenza()
        presenza.user_id = user.id

        db.session.add(presenza)
        db.session.commit()

        return redirect(url_for("main.checkin_success", username=username))

    return render_template("register.html")


@main_bp.route("/checkin", methods=["GET", "POST"])
def checkin():
    if request.method == "POST":
        username = request.form.get("username")
        user = User.query.filter_by(username=username).first()

        if not user:
            return render_template("checkin.html", error="Utente non trovato")

        today = date.today()
        already = Presenza.query.filter_by(user_id=user.id, data=today).first()

        if already:
            return render_template(
                "checkin.html", message="Hai già fatto il check-in oggi ✅"
            )

        presenza = Presenza()
        presenza.user_id = user.id
        db.session.add(presenza)
        db.session.commit()

        return render_template("checkin.html", message="Presenza registrata ✅")

    return render_template("checkin.html")


@main_bp.route("/checkin_success/<username>")
def checkin_success(username):
    return render_template("success.html", username=username)
