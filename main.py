from flask import Flask, render_template, redirect, request
from forms import Form, CatAdd
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from UserModels import create_and_save_user, get_user_from_storage, input_check, db, get_user
from CatModels import add_cat, add_cat_position, get_all_cats, get_one_cat, get_one_cat_position, remove_cat, \
    remove_position
from datetime import datetime
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():
    db.init_app(app)
    db.create_all()
    csrf = CSRFProtect()
    csrf.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


@app.route('/', methods=["GET"])
def main_page():
    cats = get_all_cats()
    try:
        if get_user_role() == 'user':
            return render_template('main.html', cats=cats, auth=True)
        elif get_user_role() == 'admin':
            return render_template('main.html', u=True, cats=cats, auth=True)
    except AttributeError:
        return render_template('main.html', u=False, cats=cats)


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
                print("New user created " + new_user.name)
            else:
                print("User already exists " + user.name)
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


@app.route('/add', methods=["GET", "POST"])
@login_required
def add_page():
    form = CatAdd()
    if request.method == 'GET':
        if get_user_role() == 'user':
            return 'у вас нет прав на создание котов йоу'
        return render_template('catAddPage.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            add_cat(form.data['name'], form.data['breed'], form.data['gender'], form.data['color'], form.data['age'])
            cat_id = get_all_cats()[-1].id
            add_cat_position(datetime.today(), form.data['cost'], cat_id)
        return redirect('/')


def get_user_role():
    return current_user._get_current_object().role


@app.route('/<int:id_cat>')
def cat_view(id_cat):
    try:
        if get_user_role() == 'user':
            return render_template('catPage.html', cat=get_one_cat(id_cat), cat_pos=get_one_cat_position(id_cat), user=True)
        elif get_user_role() == 'admin':
            return render_template('catPage.html', cat=get_one_cat(id_cat), cat_pos=get_one_cat_position(id_cat), admin=True)
    except AttributeError:
        return render_template('catPage.html', cat=get_one_cat(id_cat), cat_pos=get_one_cat_position(id_cat))


@app.route('/delete_chosen_cat', methods=['GET'])
def cat_delete():
    if request.method == 'GET':
        cat_id = request.args.get('id')
        if cat_id is None:
            print('here')
            return redirect('/')
        remove_cat(cat_id)
        remove_position(cat_id)
        return redirect('/')


if __name__ == "__main__":
    app.run()
