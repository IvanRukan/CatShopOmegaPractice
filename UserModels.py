import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, user_id, email, name, password, role):
        self.id = user_id
        self.email = email
        self.name = name
        self.password = password
        self.role = role


def create_and_save_user(form):
    email = form.data['email']
    name = form.data['name']
    password = form.data['password']
    user_id = str(numeric_value_from_string(email))[0:17]
    new_user = User(user_id, email, name, generate_password_hash(password), 'user')
    add_user(new_user.id, new_user.email, new_user.name, new_user.password, new_user.role)
    return new_user


def get_user_from_storage(form):
    email = form.data['email']
    user_id = str(numeric_value_from_string(email))[0:17]
    return get_user(user_id)


def input_check(form):
    email = form.data['email']
    user_id = str(numeric_value_from_string(email))[0:17]
    found_user = get_user(user_id)
    try:
        if check_password_hash(found_user.password, form.data['password']) and form.data['name'] == found_user.name:
            return found_user
        return             # "Неверное имя пользователя или пароль!"
    except AttributeError:
        return             # "Такого пользователя не существует!"


db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)


def add_user(id, email, name, password, role):
    user = UserModel(id=id, email=email, name=name, password=password, role=role)
    db.session.add(user)
    db.session.commit()


def get_user(id):
    user = UserModel.query.filter_by(id=id).all()
    if len(user) == 0:
        return None
    return User(user_id=user[0].id, email=user[0].email, name=user[0].name, password=user[0].password, role=user[0].role)


def numeric_value_from_string(s):
    h = hashlib.new('sha1')
    h.update(s.encode())
    hx = h.hexdigest()
    return int(hx, base=16)

# создание аккаунтов для администраторов
# def create_admin():
#     id_admin = str(numeric_value_from_string('07vanek@gmail.com'))[0:17]
#     db_admin = UserModel(id=id_admin, email='07vanek@gmail.com', name='admin', password=generate_password_hash('admin'), role='admin')
#     db.session.add(db_admin)
#     db.session.commit()

