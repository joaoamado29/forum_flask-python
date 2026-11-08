from forumJogos import app, database, bcrypt
from forumJogos.forms import FormLogin, FormCriarConta
from flask import render_template, url_for, request, flash, redirect
from forumJogos.models import Usuario, Post

lista_usuarios = ['Joao', 'Ana', 'Liliane', 'Amado'] # Temporário


@app.route('/') #decorator
def home():
    return render_template('home.html')

@app.route('/contato') #decorator
def contato():
    return render_template('contato.html')

@app.route('/users')
def users():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        # Criou usuario
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)

        # Commit usuario no BD
        database.session.add(usuario)
        database.session.commit()

        flash(f'Conta criada com sucesso no email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)