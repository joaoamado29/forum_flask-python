from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv('SECRET_TOKEN'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from forumJogos import routes