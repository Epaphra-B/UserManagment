# Flask User Management System

A full-stack **user management web application** built with **Flask**.  
Features include authentication, profile management, and admin dashboard for user control.

---

## 🚀 Features

- User Registration and Login
- Secure Password Hashing (Werkzeug)
- Role-based Access Control (`user`, `admin`)
- Admin Dashboard for managing users
- Profile Update Page
- CSRF Protection with Flask-WTF
- SQLAlchemy ORM with Flask-Migrate
- Bootstrap 5 UI

---

## 📂 Project Structure

```text

user_mgmt/
├── app.py                # Entry point
├── config.py             # Configuration
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (ignored by git)
├── migrations/           # Database migrations
└── app/
    ├── __init__.py
    ├── extensions.py
    ├── models.py
    ├── forms.py
    ├── utils.py
    ├── auth/             # Authentication routes
    ├── user/             # User profile routes
    ├── admin/            # Admin dashboard
    └── templates/        # Jinja2 templates
```

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/flask-user-management.git
cd flask-user-management
Flask Project Setup Guide
2. Create Virtual Environment
First, create and activate a virtual environment for your project.
```

### Create the virtual environment

```bash
python -m venv .venv
```

### Activate the environment

#### On macOS/Linux

```bash
source .venv/bin/activate
```

#### On Windows

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages using the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a .env file in the root of your project to store environment variables.

.env file:

```bash
FLASK_ENV=development
SECRET_KEY=change-this-32char-secret
DATABASE_URL=sqlite:///instance.db
```

### 🗄️ Database Setup

Initialize the database, create the initial migration, and apply it.

```bash
flask db init
flask db migrate -m "init users"
flask db upgrade
```

### Create Admin User

Run the following Python code to create a default administrator.

```bash
from app import create_app
from app.extensions import db
from app.models import User
app = create_app()
with app.app_context():
    u = User(username="admin", email="<admin@example.com>", role="admin")
    u.set_password("ChangeMeNow123!")
    db.session.add(u)
    db.session.commit()
```

### ▶️ Run the Application

Start the Flask development server.

```bash
flask run
```

Once running, you can access the application by navigating to <http://127.0.0.1:5000/> in your web browser.

### 🔑 Default Admin Credentials

- Username: admin

- Password: ChangeMeNow123!
