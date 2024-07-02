from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from main import db
# описывать таблицы пользователей в бд будем здесь же
temporary_storage = {}  # будет бд, это временная симуляция сохранения в словарь


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
    user_id = str(hash(email))
    new_user = User(user_id, email, name, generate_password_hash(password))
    temporary_storage[user_id] = new_user  # сохранение в бд, а не в словарь
    return new_user


def get_user_from_storage(form):
    email = form.data['email']
    user_id = str(hash(email))
    return temporary_storage.get(user_id)  # получение из бд


def input_check(form):
    email = form.data['email']
    user_id = str(hash(email))
    found_user = temporary_storage.get(user_id)
    if found_user is None:
        return None
    if check_password_hash(found_user.password, form.data['password']) and form.data['name'] == found_user.name:
        return found_user
    return "Неверное имя пользователя или пароль!"

class UserModel(db.model):
    __tablename__ = 'users'
    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)

class AdminModel(db.model):
    __tablename__ = 'admins'
    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)


db.create_all()

def getAdmin(id):
    return AdminModel.query.all()
def addUser(id, email, name, password, role):
    user = UserModel(id=id, email=email, name=name, password=password, role=role)
    db.session.add(user)
    db.session.commit()
def getUser(id):
    return UserModel.query.filter_by(id=id).all()