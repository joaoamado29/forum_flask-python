from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

lista_usuarios = ['Joao', 'Ana', 'Liliane', 'Amado']

app.config['SECRET_KEY'] = str(os.getenv('SECRET_TOKEN'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

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
        flash(f'Conta criada com sucesso no email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)