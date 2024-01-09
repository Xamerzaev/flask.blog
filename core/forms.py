from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email


class RegForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Это поле обязательно"),
            Email("Вы не правильно ввели свой майл"),
        ],
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired(message="Это поле обязательно")]
    )


class PostForm(FlaskForm):
    title = StringField(
        "Заголовок", validators=[DataRequired(message="Это поле обязательно")]
    )
    content = TextAreaField(
        "Контент", validators=[DataRequired(message="Это поле обязательно")]
    )
