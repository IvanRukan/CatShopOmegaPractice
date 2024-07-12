from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, RadioField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class Form(FlaskForm):
    email = EmailField('Введите электронную почту:', validators=[DataRequired()])
    name = StringField('Введите имя пользователя:', validators=[DataRequired()])
    password = PasswordField('Введите пароль:', validators=[DataRequired()])


class CatAdd(FlaskForm):
    name = StringField('Введите имя кота:', validators=[DataRequired()])
    breed = StringField('Введите породу кота:', validators=[DataRequired()])
    gender = RadioField('Выберите пол кота:', choices=[('м', 'Мужской'), ('ж', 'Женский')], validators=[DataRequired()])
    color = StringField('Введите цвет кота:', validators=[DataRequired()])
    age = IntegerField('Введите возраст кота:', validators=[DataRequired(), NumberRange(0, 30)])
    cost = IntegerField('Введите цену кота:', validators=[DataRequired(), NumberRange(1, 100000)])
