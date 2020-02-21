import requests
from webapp.db import db
from webapp.parsing.models import Bandcamp, SoundCloud
from config import Config
import logging

logger = logging.getLogger(__name__)


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.json()
    except(requests.RequestException, ValueError) as error:
        logger.error(error)
        print('Сетевая ошибка, смотреть логфайл')
        return False

def create_url(url, data_from_form):
    url = [f'{url}{data_from_form}']
    data = Config.SC_DATA_SEARCH
    for i in data:
        url.append(f"{i}={data[i]}")
    return "&".join(url)


def save_bandcamp(genre, art, author, title, music_url, date_entry):
    playlist_exists = Bandcamp.query.filter(Bandcamp.title == title).count()
    if not playlist_exists:
        new_playlist = Bandcamp(genre=genre,
                                art=art,
                                author=author,
                                title=title,
                                music_url=music_url,
                                date_entry=date_entry)
        db.session.add(new_playlist)
        db.session.commit()


def save_soundcloud(genre, art, author, title, music_url, date_entry):
    playlist_exists = SoundCloud.query.filter(SoundCloud.title == title).count()
    if not playlist_exists:
        new_playlist = SoundCloud(genre=genre, 
                                  art=art,
                                  author=author,
                                  title=title,
                                  music_url=music_url,
                                  date_entry=date_entry)
        db.session.add(new_playlist)
        db.session.commit()