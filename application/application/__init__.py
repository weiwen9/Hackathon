from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
DB_NAME = "DataBase.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
