import hashlib

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# описывать таблицы пользователей в бд будем здесь же
# temporary_storage = {}  # будет бд, это временная симуляция сохранения в словарь


class User(UserMixin):
    def __init__(self, user_id, email, name, password):
        self.id = user_id
        self.email = email
        self.name = name
        self.password = password
        self.role = 'user'


class Admin(UserMixin):
    def __init__(self, user_id, email, name, password):
        self.id = user_id
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
        self.role = 'admin'


def create_and_save_user(form):
    email = form.data['email']
    name = form.data['name']
    password = form.data['password']
    user_id = str(numericvalue_from_string(email))[0:17]
    new_user = User(user_id, email, name, generate_password_hash(password))
    add_user(new_user.id, new_user.email, new_user.name, new_user.password, new_user.role)
    #temporary_storage[user_id] = new_user  # сохранение в бд, а не в словарь
    return new_user


def get_user_from_storage(form):
    email = form.data['email']
    user_id = str(numericvalue_from_string(email))[0:17]
    #return temporary_storage.get(user_id)  # получение из бд
    return get_user(user_id)


def input_check(form):
    email = form.data['email']
    user_id = str(numericvalue_from_string(email))[0:17]
    #found_user = temporary_storage.get(user_id)  # получение из бд
    found_user = get_user(user_id)
    print(found_user.password)
    if check_password_hash(found_user.password, form.data['password']) and form.data['name'] == found_user.name:
        return found_user
    return None

db = SQLAlchemy()
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)


class AdminModel(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)




def get_admin(id):
    return AdminModel.query.all()


def add_user(id, email, name, password, role):
    user = UserModel(id=id, email=email, name=name, password=password, role=role)
    db.session.add(user)
    db.session.commit()


def get_user(id):
    user = UserModel.query.filter_by(id=id).all()
    print(len(user))
    print(id)
    if len(user) == 0:
        return None
    return User(user_id=user[0].id, email=user[0].email, name=user[0].name, password=user[0].password)

def numericvalue_from_string(s):
    h = hashlib.new('sha1') #for shortest results with sha, if you are ok with big numbers then sha256 or sha512 also work.
    h.update(s.encode())
    hx = h.hexdigest()
    return int(hx, base=16)