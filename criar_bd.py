from forumJogos import app, database
from forumJogos.models import Usuario, Post

with app.app_context(database):
    database.create_all()