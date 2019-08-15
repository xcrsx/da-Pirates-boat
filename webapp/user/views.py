from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from webapp import login_
from webapp.db import db
from webapp.user.models import Favorite, User
from werkzeug.urls import url_parse
from webapp.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome back!')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user.index')
        return redirect(next_page)
    return render_template('user/login.html', title='Sign In', form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.index'))


@blueprint.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    songs = Favorite.query.filter_by(user_id=user.id).all()
    return render_template('user/profile.html', title='My profile', user=user,
                           songs=songs)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to da Boat!')
        return redirect(url_for('user.index'))
    return render_template('user/register.html', title='Register', form=form)


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    user = current_user
    form = LoginForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('user.login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('user.index'))
    return render_template('index.html', title='Wharf', form=form)


@blueprint.route('/add_song', methods=['POST', 'GET'])
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
