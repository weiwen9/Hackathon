from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
DB_NAME = "DataBase.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User Model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Redirect to the user's home page after successful login
            return redirect(url_for("home"))
        else:
            # Flash an error message and render the login template
            flash("Invalid credentials. Please try again.", "error")

    return render_template("login.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        # Check whether email or username already exists in the database
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        # Flash messages based on input
        if existing_email:
            flash("Email already exists!", "error")
        elif existing_user:
            flash("Username already exists!", "error")
        elif password != password2:
            flash("Passwords do not match!", "error")
        else:
            # Hash password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Create new user and store data
            new_user = User(email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            # Flash successful sign-up message
            flash("Account successfully created!", "success")

        return render_template('login.html')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
