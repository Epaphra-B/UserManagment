from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        
        # Hash the password
        hashed_password = ph.hash(password)
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email address already exists!', 'error')
            return redirect(url_for('add_user'))
        
        # Create new user
        new_user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=hashed_password
        )
        
        # Add to database
        db.session.add(new_user)
        db.session.commit()
        
        flash('User added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_user.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        # Update user data
        user.firstname = request.form['firstname']
        user.lastname = request.form['lastname']
        user.email = request.form['email']
        
        # Only update password if a new one was provided
        if request.form['password']:
            user.password = ph.hash(request.form['password'])
        
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)