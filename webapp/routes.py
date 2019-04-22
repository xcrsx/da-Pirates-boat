from webapp.db import db
from flask import render_template, flash, redirect, url_for, request
from webapp import app, login
from flask_login import current_user, login_user, login_required
from webapp.parsing.models import Bandcamp, SoundCloud
from webapp.user.models import User, Favorite
from webapp.user.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
def index():
    user = current_user
    form = LoginForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('user/user.login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
    return render_template('index.html', title='Wharf', form=form)


@app.route('/add_song', methods=['POST'])
@login_required
def add_song():
    song = request.form['song']
    user = current_user
    song_in_db = Favorite.query.filter_by(song=song, user_id=user.id).first()
    if not song_in_db:
        new_song = Favorite(song=song, user_id=user.id)
    db.session.add(new_song)
    db.session.commit()
    flash('You are have added the song to you favorite')
    return redirect(url_for('index'))


@app.route('/remove_song', methods=['POST'])
def remove_song():
    song = request.form['song']
    user = current_user
    title = Favorite.query.filter_by(song=song, user_id=user.id).first()
    db.session.delete(title)
    db.session.commit()
    flash('You are have removed the song from you favorite')
    return redirect(url_for('index'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

