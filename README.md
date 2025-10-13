## 🚀 Attività UFO - Activity Tracker

Un'app web leggera per tracciare le presenze tramite QR code, sviluppata con Flask e SQLAlchemy. Ideale per gestire le attività di UFO Saronno.

### ⚙️ Funzionalità

- Registrazione studenti:

  - Nome e cognome
  - Scuola
  - Classe
  - Username univoco

- Check-in giornaliero tramite username

- Database SQLite per salvare le presenze

- Admin panel protetto da login per visualizzare e gestire i dati

### 🛠️ Tecnologie

- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- HTML/CSS

### 🚀 Avvio rapido

1. Clona la repo:

   ```bash
   git clone https://github.com/acrazypie/attivita_ufo.git
   cd attivita_ufo
   ```

2. Installa le dipendenze:

   ```bash
   pip install -r requirements.txt
   ```

3. Avvia l'app:

   ```bash
   python app.py
   ```

4. Accedi all'app su http://localhost:5000

### 🔐 Accesso Admin

- Username: admin
- Password: admin123

### 📂 Struttura del progetto

```
attivita_ufo/
├── app.py          # Entry point dell'app
├── models.py       # Definizione dei modelli
├── routes/         # Gestione delle rotte
├── db/             # Database SQLite (generato automaticamente)
├── static/         # File statici (CSS, JS, immagini)
├── templates/      # Template HTML
├── utils/          # Funzioni di utilità
├── requirements.txt # Dipendenze del progetto
└── README.md       # Questo file
```

### 📄 Licenza

Distribuito sotto la licenza MIT. Vedi il file LICENSE per i dettagli.
