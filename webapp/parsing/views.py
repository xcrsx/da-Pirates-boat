from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import current_user, login_user, login_required
from webapp.parsing.bc_parsing import bandcamp_parsing
from webapp.parsing.sc_parsing import soundcloud_parsing
from webapp.parsing.models import Bandcamp, SoundCloud
from webapp.user.forms import LoginForm
from webapp.user.models import User, Favorite
from webapp.db import db


blueprint = Blueprint('parsing', __name__)


@blueprint.route('/')
def parsing():
    form = LoginForm()
    bandcamp_parsing()
    soundcloud_parsing()
    popular_sc = SoundCloud.query.order_by(SoundCloud.date_entry.desc()).limit(8).all()
    popular_bc = Bandcamp.query.order_by(Bandcamp.date_entry.desc()).limit(20).all()
    return render_template('index.html', popular_sc=popular_sc, popular_bc=popular_bc, form=form)


@blueprint.route('/add_song', methods=['POST'])
@login_required
def add_song():
    song = request.form['song']
    user = current_user
    new_song = Favorite(song=song, user_id=user.id)
    db.session.add(new_song)
    db.session.commit()
    flash('You are have added the song to you favorite')
    return redirect(url_for('user.index'))


@blueprint.route('/remove_song', methods=['POST'])
def remove_song():
    song = request.form['song']
    user = current_user
    title = Favorite.query.filter_by(song=song, user_id=user.id).first()
    db.session.delete(title)
    db.session.commit()
    flash('You are have removed the song from you favorite')
    return redirect(url_for('user.index'))

