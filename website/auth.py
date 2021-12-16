from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from .models import *
from .sendemail import send

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.values.get('username')
        password = request.values.get('password')
        cur.execute("SELECT senha FROM Usuario WHERE username = '{}'".format(user))
        pskey = cur.fetchall()
        try:
            if len(user) < 4:
                flash('O nome de usuário deve ter no mínimo 4 caracteres!', category='error')
            elif len(password) < 6:
                flash('A senha deve ter no mínimo 6 caracteres!', category='error')
            elif password != pskey[0][0]:
                flash('Senha incorreta!', category='error')
            else:
                return redirect(url_for('views.main'))
        except psycopg2.DatabaseError:
            flash('Verifique se o usuario informado está correto!', category='error')

    return render_template('login.html')


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.values.get('username')
        email = request.values.get('email')
        password = request.values.get('password')
        msgUser = 'O nome de usuário deve ter no mínimo 4 caracteres'
        msgPassword = 'A senha deve ter no mínimo 6 caracteres'
        try:
            if len(username) < 4:
                flash(msgUser, category='error')
            elif len(password) < 6:
                flash(msgPassword, category='error')
            else:
                User.createNewUser(User(username, email, password))
                flash('Usuario Criado com sucesso!', category='success')
        except psycopg2.DatabaseError:
            flash('O email informado já está em uso!', category='error')

            
    return render_template('signin.html')


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    try:
        if request.method == 'POST':
            email = request.values.get('email')
            cur.execute("SELECT username FROM Usuario WHERE email = '{}'".format(email))
            user = cur.fetchall()
            cur.execute("SELECT senha FROM Usuario WHERE email = '{}'".format(email))
            pw = cur.fetchall()
            user = user[0][0]
            pw = pw[0][0]
            send.sendEmail(email, user, pw)
            flash('Enviamos a informação para o email informado!', category='success')
            print('ok')
        else:
            pass
    except psycopg2.DatabaseError:
            flash('O email informado não existe!', category='error')
    return render_template('forgot.html')