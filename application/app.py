from flask import Flask
from application import db
from application.views import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '!1ONEone'
DB_NAME = "DataBase.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

if __name__ == '__main__':
    app.run(debug=True)
