from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class AddPostForm(FlaskForm):
    name_user = StringField('Имя', validators=[DataRequired()])
    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Пост', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class AddCommentForm(FlaskForm):
    comment = StringField('None', validators=[DataRequired()])
    id = HiddenField()
    submit = SubmitField('Отправить')