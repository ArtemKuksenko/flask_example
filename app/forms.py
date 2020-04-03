from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name_user = StringField('Имя', validators=[DataRequired()])
    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Пост', validators=[DataRequired()])

    submit = SubmitField('Отправить')