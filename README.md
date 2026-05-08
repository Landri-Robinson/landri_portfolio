# Landri Robinson — AI Portfolio
## Setup Instructions

Follow these steps to get the site running on your computer.

---

## Step 1 — Check if Python is installed

Open your terminal (Mac) or Command Prompt (Windows) and type:

```
python --version
```

If you see a version number (3.10 or higher), you're good. If not, download Python from https://www.python.org/downloads/ — make sure to check "Add Python to PATH" during install.

---

## Step 2 — Open the project in VS Code

1. Open VS Code
2. Go to File → Open Folder
3. Select the `landri_portfolio` folder you extracted from the zip

---

## Step 3 — Open the terminal in VS Code

Go to Terminal → New Terminal in VS Code.

---

## Step 4 — Create a virtual environment

```
python -m venv venv
```

Then activate it:

- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

You should see `(venv)` appear in your terminal prompt.

---

## Step 5 — Install dependencies

```
pip install -r requirements.txt
```

---

## Step 6 — Set up the database

```
python manage.py migrate
```

---

## Step 7 — Load the placeholder project data

```
python manage.py loaddata portfolio/fixtures/initial_data.json
```

This loads all 6 placeholder projects and your skills into the database.

---

## Step 8 — Create your admin account

```
python manage.py createsuperuser
```

Enter a username, email (optional), and password when prompted.

---

## Step 9 — Run the server

```
python manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000**

---

## Step 10 — Access the admin panel

Go to: **http://127.0.0.1:8000/admin**

Log in with the superuser account you just created. From here you can:
- Edit any of the 6 placeholder projects with your real content
- Upload your screenshots
- Add your experience and education
- Update your skills

---

## Folder Structure

```
landri_portfolio/
├── config/          # Django settings, URLs
├── portfolio/       # Main app (models, views, templates)
│   ├── fixtures/    # Placeholder data
│   ├── templates/   # All HTML pages
├── static/
│   └── css/         # Custom stylesheet
├── media/           # Uploaded images (created after first upload)
├── manage.py
├── requirements.txt
└── README.md
```

---

## Common Issues

**"No module named django"** — Make sure your virtual environment is activated (`source venv/bin/activate` or `venv\Scripts\activate`)

**Port already in use** — Try `python manage.py runserver 8080` and visit http://127.0.0.1:8080

**Images not showing** — Make sure you ran `python manage.py migrate` and that DEBUG=True in settings.py
