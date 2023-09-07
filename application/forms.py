from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from application.models import User
from flask import flash

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

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")
