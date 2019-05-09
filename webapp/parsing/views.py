from flask import Blueprint, render_template
from webapp.parsing.bc_parsing import bandcamp_parsing
from webapp.parsing.sc_parsing import soundcloud_parsing
from webapp.parsing.models import Bandcamp, SoundCloud
from webapp.user.forms import LoginForm


blueprint = Blueprint('parsing', __name__, url_prefix='/users')


@blueprint.route('/')
def parsing():
    bandcamp_parsing()
    soundcloud_parsing()
    popular_sc = SoundCloud.query.limit(8).all()
    popular_bc = Bandcamp.query.limit(20).all()
    return render_template('index.html', popular_sc=popular_sc,
                           popular_bc=popular_bc)
