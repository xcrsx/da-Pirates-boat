from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={"class": "form-control",
                           "id": "exampleInputUsername1",
                           "placeholder": "Enter your username"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"class": "form-control",
                             "id": "exampleInputPassword1",
                             "placeholder": "Enter password"})
    remember_me = BooleanField('Remember',)
    submit = SubmitField('Sign In', render_kw={"class": "btn btn-primary"})


class MusicSearchForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("I'm looking for...", validators=[DataRequired()],
                         render_kw={"class": "form-control",
                         "id": "exampleInputRequest",
                         "placeholder": "Search for artist or song"})
    submit = SubmitField('Find it!!!')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),
                              EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different enail adress.')
    submit = SubmitField('Register')


""" Пока так, в дальнейшем в search_result_form добавить парсинг и вывод имен,
альбмов, треков """


class SearchResultForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("Did not you find what you were looking for?",
                         validators=[DataRequired()])
    submit = SubmitField('Try again!')
