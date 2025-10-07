# Attività UFO - Activity Tracker

Un'applicazione web leggera per tracciare le presenze tramite QR code, costruita con Flask e SQLAlchemy.

## 📝 Funzionalità

* Registrazione studenti con:

  * Nome e cognome
  * Scuola
  * Classe
  * Username univoco
* Check-in giornaliero tramite username
* Database SQLite per salvare presenze
* Admin panel protetto da login:

  * Visualizzazione presenze di ogni utente
  * Esportazione presenze in CSV
* Sistema leggero

## 💻 Tecnologie

* Python 3.10+
* Flask
* Flask-Login
* SQLAlchemy
* SQLite
* HTML/Jinja templates
* TailwindCSS (opzionale per lo stile)

## 📁 Struttura progetto

```
/aulastudio
├── app.py                     # Entrypoint principale Flask
├── models.py                  # Modelli SQLAlchemy
├── /routes
│   ├── __init__.py
│   ├── main.py                # Rotte pubbliche
│   ├── admin.py               # Rotte admin
├── /utils
│   ├── export.py              # Funzione esportazione CSV
├── /templates                 # Pagine HTML
├── /static                    # File CSS/JS
├── /instance
│   └── aulastudio.db          # Database SQLite
├── requirements.txt
└── config.py
```

## ⚙️ Installazione

1. Clona il repository:

```bash
git clone https://github.com/acrazypie/attivita_ufo.git
cd attivita_ufo
```

2. Crea un ambiente virtuale e installa le dipendenze:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

3. Crea il database e l’admin iniziale:

```bash
python
>>> from app import create_app, db
>>> from models import Admin
>>> app = create_app()
>>> with app.app_context():
...     admin = Admin(username='admin')
...     admin.set_password('PasswordMoltoSicura123')
...     db.session.add(admin)
...     db.session.commit()
```

4. Avvia l’app:

```bash
flask run
```

L’app sarà disponibile su `http://127.0.0.1:5000`.

## 🔐 Login Admin

* URL: `/admin/login`
* Credenziali iniziali: `admin` / `PasswordMoltoSicura123`
* Consente di visualizzare utenti, presenze e scaricare CSV.

## 📄 Note

* L’app può funzionare interamente in locale senza CORS.
* Puoi aggiungere uno stile con TailwindCSS o qualsiasi altro framework CSS.
* Per produzione, assicurati di usare un secret key sicuro e considerare un database più robusto di SQLite.

## 🛠 Estensioni future

* Grafici statistiche presenze
* Notifiche automatiche via email/Telegram
* Multi-aula e gestione classi avanzata

## ⚖️ Licenza

MIT License
