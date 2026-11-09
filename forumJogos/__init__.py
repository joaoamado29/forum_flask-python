from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv('SECRET_TOKEN'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Acesso não autorizado! Login necessário.'
login_manager.login_message_category = 'alert-info'

from forumJogos import routes