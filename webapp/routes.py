from webapp import db
from flask import render_template, flash, redirect, url_for, request
from webapp import app, login
from flask_login import current_user, login_user, login_required
from webapp.models import Favorite, Popular, Bandcamp
from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.sc_parsing import soundcloud_parsing
from webapp.bc_parsing import bandcamp_parsing




@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = current_user
    soundcloud_parsing()
    bandcamp_parsing()
#    sc_list = SoundCloudParsing.sc_result
    popular_sc = Popular.query.limit(8).all()
    popular_bc = Bandcamp.query.limit(20).all()
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
                           popular_sc=popular_sc, popular_bc=popular_bc)


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


@app.route('/add_song', methods=['POST'])
@login_required
def add_song():
    song = request.form['song']
    user = current_user
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

