from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta
import os

app = Flask(__name__)

lista_usuarios = ['Joao', 'Ana', 'Liliane', 'Amado']

app.config['SECRET_KEY'] = str(os.getenv('SECRET_TOKEN'))

@app.route('/') #decorator
def home():
    return render_template('home.html')

@app.route('/contato') #decorator
def contato():
    return render_template('contato.html')

@app.route('/users')
def users():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)