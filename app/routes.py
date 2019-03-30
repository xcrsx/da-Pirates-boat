from app import db
from app.forms import RegistrationForm
from flask import render_template, flash, redirect, url_for, request
from app import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Favorite, Popular
from werkzeug.urls import url_parse
from app.forms import LoginForm, MusicSearchForm, SearchResultForm
from app.sc_parsing import soundcloud_parsing
from app.bc_parsing import get_daily_music


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = current_user
    soundcloud_parsing()
#    sc_list = SoundCloudParsing.sc_result
    popular_sc = Popular.query.order_by(Popular.timestamp.desc()).limit(6).all()
    bc_list = get_daily_music()
    form = LoginForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
    return render_template('index.html', title='Wharf', form=form,
                           popular_sc=popular_sc, bc_list=bc_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome back!')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = MusicSearchForm()
    if form.validate_on_submit():
        flash('Search requested for author: {}'.format(
           form.search.data))
        return redirect('/search_result')
    return render_template('search.html', title="Let's find smth", form=form)


@app.route('/search_result', methods=['GET', 'POST'])
def search_result():
    form = SearchResultForm()
    if form.validate_on_submit():
        flash('New search requested: {}'.format(
           form.search.data))
        return redirect('/search_result')
    return render_template('search_result.html', title="Let's find smth", 
                           form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    artists = Favorite.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', title='My profile', user=user,
                           artists=artists)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


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
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/player')
def player():
    title = SoundCloudParsing.sc_title
    return render_template('player.html', title=title)
