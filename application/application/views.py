from flask import render_template, request, redirect, url_for, flash
from application import app, db, bcrypt
from application.models import User
from application.forms import SignupForm, LoginForm

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
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
            flash("Invalid credentials. Please try again.", "error")

    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
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
