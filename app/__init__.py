from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'dea094e27413f73f418d9f0c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import routes
