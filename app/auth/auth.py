from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models.usuarios import Usuarios
from shared.db import db

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email       = request.form.get('email')
    password    = request.form.get('password')
    remember    = True # Adicionar este campo a view depois

    user = Usuarios.query.filter_by(email=email).first()

    """ if not user or not check_password_hash(user.password, password):
        flash("Usuário e/ou senha inválidos. Verifique.", 'error')
        return redirect(url_for('auth.login')) """

    login_user(user, remember=remember)

    return "LOGOU" #redirect(url_for('main.home'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
