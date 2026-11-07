from main import database
from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post', backref='autor', lazy=True)
    jogo = database.Column(database.String, default='Não Especificado.')

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=utc_now)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)