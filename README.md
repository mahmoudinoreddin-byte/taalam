# Portfòlio Platform

A modern CV & portfolio platform — Django + Tailwind CSS.

---

## Deploy on Railway (5 minutes)

### Step 1 — Push to GitHub
1. Create a free account on [github.com](https://github.com)
2. Create a new repository (public or private)
3. Upload all project files (drag & drop ZIP or use Git)

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourname/portfolio-platform.git
git push -u origin main
```

### Step 2 — Deploy on Railway
1. Go to [railway.app](https://railway.app) → Sign up free
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your repository
4. Railway auto-detects Django and starts building

### Step 3 — Set environment variables
In Railway dashboard → your project → **Variables** tab, add:

| Variable | Value |
|---|---|
| `SECRET_KEY` | any long random string (e.g. `abc123xyz...50chars`) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.railway.app,localhost` |

### Step 4 — Create admin user
In Railway → your project → **Deploy** tab → click **Open Shell**:
```bash
python manage.py createsuperuser
```

### Step 5 — Open your site
Railway gives you a URL like `https://portfolio-platform-production.up.railway.app`

Your admin panel: `https://your-url.railway.app/admin`

---

## Local Development

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: http://127.0.0.1:8000

---

## Project Structure

```
portfolio_platform/
├── manage.py
├── requirements.txt        # Dependencies
├── Procfile                # Railway/Heroku start command
├── railway.json            # Railway config
├── nixpacks.toml           # Build config
├── runtime.txt             # Python version
├── .env.example            # Copy to .env for local dev
├── .gitignore
├── portfolio_platform/     # Django config (settings, urls)
├── accounts/               # Auth + custom User model
├── profiles/               # CV editor + public profile /p/<username>/
├── shop/                   # Products + orders
├── lms/                    # Courses + lessons + progress
├── messaging/              # Direct messages
├── templates/              # All HTML pages
├── static/                 # CSS / JS / images
└── media/                  # User uploads
```

---

## Key URLs

| URL | Description |
|---|---|
| `/` | Landing page |
| `/accounts/register/` | Sign up |
| `/profiles/dashboard/` | Profile editor |
| `/p/<username>/` | Public profile (shareable link) |
| `/shop/` | Product shop |
| `/lms/` | Courses |
| `/messages/inbox/` | Messaging |
| `/admin/` | Admin panel |

---

## Add content via Admin

Go to `/admin/` after creating a superuser.

- **Shop products** → Shop → Products → Add Product
- **Courses** → Lms → Courses → Add Course (add lessons inline)
- **User profiles** → Profiles → Profiles

---

## Tech Stack

- Django 4.2 · SQLite (dev) / PostgreSQL (prod)
- Tailwind CSS via CDN
- WhiteNoise for static files
- Gunicorn WSGI server
- Deployed on Railway
