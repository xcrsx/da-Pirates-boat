from flask import Blueprint, render_template, flash, redirect, url_for
from webapp.search.forms import MusicSearchForm
from webapp.search_in_sc import search_sc

blueprint = Blueprint('search', __name__, url_prefix='/searching')


@blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = MusicSearchForm()
    if form.validate_on_submit():
        flash('Search requested for author: {}'.format(
           form.search.data))
        return redirect(url_for('search.search_result'))
    return render_template('search.html', title="Let's find smth", form=form)


@blueprint.route('/search_result', methods=['GET', 'POST'])
def search_result():
    list_of_songs = search_sc()
    return render_template('search_result.html', title="what do we have here",
                           list_of_songs=list_of_songs)
