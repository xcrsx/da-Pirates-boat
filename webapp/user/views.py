from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import Favorite
from webapp.user.models import User
from werkzeug.urls import url_parse
from webapp.user.forms import LoginForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@blueprint.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    songs = Favorite.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', title='My profile', user=user,
                           songs=songs)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))