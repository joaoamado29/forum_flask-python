# from forumJogos import app, database
# from forumJogos.models import Usuario, Post

# with app.app_context():
#     database.create_all()

#with app.app_context():
    #usuario = Usuario(username='Joao Amado', email='amadao@gmail.com', senha='pao123')
    #usuario2 = Usuario(username='Lima', email='Limao@gmail.com', senha='leao123')

    #database.session.add(usuario)
    #database.session.add(usuario2)

    #database.session.commit()

#with app.app_context():
    #meus_usuario = Usuario.query.all()
    #print(meus_usuario)
    #print(meus_usuario[1].username)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Free PDL', corpo='Essa build de Talon é a melhor dos ultimos anos, free pdl, estou com 13 vitorias seguidas.')
#     database.session.add(meu_post)
#     database.session.commit()


# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)/