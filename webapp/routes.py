from webapp import db
from flask import render_template, flash, redirect, url_for
from webapp import app, login
from flask_login import current_user, login_user, login_required
from webapp.models import Favorite, Popular
from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.sc_parsing import soundcloud_parsing
from webapp.bc_parsing import get_daily_music


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = current_user
    soundcloud_parsing()
#    sc_list = SoundCloudParsing.sc_result
    popular_sc = Popular.query.limit(6).all()
    bc_list = get_daily_music()
    form = LoginForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('user.login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
    return render_template('index.html', title='Wharf', form=form,
                           popular_sc=popular_sc, bc_list=bc_list)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to da Boat!')
        return redirect(url_for('user.login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song(song):
    title = Favorite.query.filter_by(song=song).first()
    current_user.add_to_favorite(title)
    db.session.commit()
    flash('You are have added the song to you favorite')
    return redirect(url_for('user'))


@app.route('/remove_song', methods=['GET', 'POST'])
def remove_song(song):
    title = Favorite.query.filter_by(song=song).first()
    current_user.remove_from_favorite(title)
    db.session.commit()
    flash('You are have removed the song from you favorite')
    return redirect(url_for('user'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))