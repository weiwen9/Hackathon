from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
import time


app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = '!1ONEone'
DB_NAME = "DataBase.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Define Signup Form
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # To check whether username or email is already in use
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            flash("Username already exists!", "error")
            raise ValidationError("Username already exists!")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            flash("Email already exists!", "error")
            raise ValidationError("Email already exists!")

# Define Login Form Model
class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


# Create database tables
with app.app_context():
    db.create_all()


# Defining routes
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data

        # Authenticate user
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Redirect to home page if passwords match
            return redirect(url_for("home"))
        else:
            # Flash an error message and Render the login template
            wrong_password = True

    return render_template("/login.html", form=form)


@app.route('/home.html')
def home():
    return render_template("home.html")


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    
    if request.method == 'POST':
        # Check whether data provided are valid
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # Hash password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Create new user and store data
            new_user = User(email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            # Flash successful sign-up message
            flash("Account successfully created!", "success")

        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)