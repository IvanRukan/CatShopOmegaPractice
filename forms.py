from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    email = EmailField('Введите электронную почту:', validators=[DataRequired()])
    name = StringField('Введите имя пользователя:', validators=[DataRequired()])
    password = PasswordField('Введите пароль:', validators=[DataRequired()])


# def extract_data(form):
#     if form.validate_on_submit():
#         email = form.data['email']
#         name = form.data['name']
#         password = form.data['password']
#         print(email, name, password)
