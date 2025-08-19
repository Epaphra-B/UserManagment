
# User Management System

A simple **Flask-based web application** for managing users.  
It allows administrators to **add, view, edit, and delete users**, with secure password storage using **Argon2 hashing**.

---

## Features

- View all registered users in a table  
- Add new users (first name, last name, email, password)  
- Edit existing users (update details, change password if needed)  
- Delete users with confirmation  
- Passwords stored securely with **Argon2**  
- Flash messages for user actions (success/error)  
- Bootstrap-powered responsive UI  

---

## Tech Stack

- **Backend:** Flask (Python)  
- **Database:** SQLite (via SQLAlchemy ORM)  
- **Security:** Argon2 for password hashing  
- **Frontend:** Jinja2 templates + Bootstrap 5  

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Epaphra-B/UserManagment.git
   cd UserManagment
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, install manually:

```bash
pip install flask flask_sqlalchemy argon2-cffi
```

4. **Run the application**

```bash
python app.py
```

5. **Access in your browser**

```bash
http://127.0.0.1:5000/
```



---

###Database Schema

The application defines a single User model:

**Field	Type	Constraints***

```text
id	Integer	Primary key
firstname	String(100)	Required
lastname	String(100)	Required
email	String(150)	Required, Unique
password	String(200)	Required (hashed via Argon2)
```


---

###Project Structure

```text
UserManagment/
│── app.py             # Main Flask application (routes, logic)
│── models.py          # Database models (User schema)
│── templates/         # HTML templates
│   ├── base.html      # Shared layout (Bootstrap, flash messages, delete confirm)
│   ├── index.html     # List of users
│   ├── add_user.html  # Add new user form
│   └── edit_user.html # Edit user form
│── database.db        # SQLite database (created automatically)
│── requirements.txt   # Python dependencies (recommended)
└── README.md          # Project documentation
```

---

###Security Notes

Passwords are hashed using Argon2 for strong protection.

Update the SECRET_KEY in app.py before deploying:

```bash
app.config['SECRET_KEY'] = 'replace-with-a-strong-secret-key'
```

For demonstration, the index.html currently shows hashed passwords.



---



