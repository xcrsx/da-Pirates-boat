from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class MusicSearchForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("I'm looking for...", validators=[DataRequired()],
                         render_kw={"class": "form-control",
                         "id": "exampleInputRequest",
                         "placeholder": "Search for artist or song"})
    submit = SubmitField('Find it!!!')


class SearchResultForm(FlaskForm):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album')]
    select = SelectField(choices=choices)
    search = StringField("Did not you find what you were looking for?",
                         validators=[DataRequired()])
    submit = SubmitField('Try again!')