# ✅ To-Do & Productivity Tracker

Preprost todo-tracker, zgrajen v Pythonu z uporabo FastAPI in Jinja2.  
Aplikacija omogoča dodajanje, označevanje in brisanje nalog ter spremljanje produktivnosti.

---

## 🚀 Hitri zagon z Docker Compose

1. Kloniraj projekt:

```bash
git clone https://github.com/matevzkalcic/NUKS-projekt
cd NUKS-projekt
```

2. Zaženi aplikacijo:

```bash
docker compose up --build
```

3. Odpri aplikacijo v brskalniku:

```
http://localhost:8000
```

---

## ⚙️ Tehnologije

- **Backend:** FastAPI (Python)
- **Frontend:** Jinja2 (HTML templating)
- **Baza:** SQLite
- **Deploy:** Docker & Docker Compose

---

## 📂 Struktura projekta

```
todo-tracker/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── templates/
│   │   └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## ✍️ Avtor

Projekt ustvarjen za učenje, testiranje in predstavitev osnovnih principov spletne aplikacije s FastAPI + Docker.
