from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv('SECRET_TOKEN'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from forumJogos import routes