from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import Form
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from UserModels import create_and_save_user, get_user_from_storage, input_check, temporary_storage
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_db.db'
db = SQLAlchemy(app)
csrf = CSRFProtect()
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return temporary_storage.get(user_id)  # импорт функции обращения к бд


@app.route('/', methods=["GET"])
def main_page():
    try:
        if current_user._get_current_object().role == 'user':    # разные функции в зависимости от роли
            return render_template('main.html', u=True, cats=[], auth=True)
        elif current_user._get_current_object().role == 'admin':
            return 'вошли в роль админа'
    except AttributeError:
        return render_template('main.html', u=False, cats=[])


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = Form()
    if request.method == 'GET':
        return render_template('form.html', form=form, browser_title="Регистрация пользователя:")
    if request.method == 'POST':
        if form.validate_on_submit():
            user = get_user_from_storage(form)
            if user is None:
                new_user = create_and_save_user(form)
                print("New user created" + new_user.name)
            else:
                print("User already exists" + user.name)
        return redirect('/')


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = Form()
    if request.method == 'GET':
        return render_template('form.html', form=form, browser_title="Вход в аккаунт:")
    if request.method == 'POST':
        if form.validate_on_submit():
            user = input_check(form)
            if user is not None:
                login_user(user)
                print('logged in')
                return redirect('/')
            else:
                print("no such user")
        else:
            print('login_failed')
        return redirect('/')


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout_page():
    logout_user()
    return redirect('/')


if __name__ == "__main__":
    app.run()
