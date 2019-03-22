from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, MusicSearchForm, SearchResultForm
from app.SC import SoundCloudParsing



@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    sc_list = SoundCloudParsing.sc_result
    user = {'username': 'mock'}
    posts = [  # it will be the popular and new music
        {
            'author': {'name': 'John'},
            'album': 'Some title'
        },
        {
            'author': {'name': 'Susan'},
            'album': 'another title'
        }
    ]
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('index.html', title='Wharf', user=user, posts=posts,
                           form=form, sc_list=sc_list)     


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')        
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
    return render_template('search_result.html', title="Let's find smth", form=form)


@app.route('/profile')
def profile():
    user = {'username': 'mock'}
    return render_template('profile.html', title='My profile', user=user)
