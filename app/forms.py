from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired






class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember')
    submit = SubmitField('Sign In')


class MusicSearchForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("I'm looking for...", validators=[DataRequired()])
    submit = SubmitField('Find it!')

""" Пока так, в дальнейшем в search_result_form добавить парсинг и вывод имен, альбмов, треков """

class SearchResultForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("Did not you find what you were looking for?", validators=[DataRequired()])
    submit = SubmitField('Try again!')




