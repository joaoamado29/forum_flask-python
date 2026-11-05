from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[
        DataRequired(),
        ])
    
    email = StringField('Email', validators=[
        DataRequired(), 
        Email()
        ])
    
    senha = PasswordField('Senha', validators=[
        DataRequired(), 
        Length(6, 20)
        ])
    
    confirmacao = PasswordField('Confirmação da Senha', validators=[
        DataRequired(), 
        EqualTo('senha')
        ])
    
    botao_submit_criarconta = SubmitField('Criar Conta', validators=[
        DataRequired(), 
        
        ])

# Classe de Login
class FormLogin(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Email()
        ])

    senha = PasswordField('Senha', validators=[
        DataRequired(), 
        Length(6, 20)
        ])

    lembrar_dados = BooleanField('Lembrar login')

    botao_submit_login = SubmitField('Login', validators=[
        DataRequired(),
        ])
