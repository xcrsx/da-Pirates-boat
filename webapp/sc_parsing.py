import requests
from config import Config
from webapp.models import Popular
from webapp.models import db


def soundcloud_parsing():
    soundcload_main_url = Config.SC_API_MAINPAGE
    result = requests.get(soundcload_main_url)
    result = result.json()
    sc_result = []
    for info in result['collection']:
        try:
            if info['genre'] == "":
                sc_genre = 'Other'
            else:
                sc_genre = info['genre']
            sc_title = info['title']
            sc_permalink_url = info['permalink_url'] #playlist
            sc_uri = info['uri']
            if info['artwork_url'] is None:
                sc_artwork_url = info['user']['avatar_url']
            else:
                sc_artwork_url = info['artwork_url'] #jpg обложки
            sc_result.append({
                'genre': sc_genre,
                'title': sc_title,
                'artwork': sc_artwork_url,
                'playlist': sc_permalink_url, # ссылка на плейлист, если он нужен. Если не нужен-можно убрать
                'uri': sc_uri
            })
        except (KeyError, ValueError):
            'Ошибка при подключении к главной странице SoundCloud'
    save_result(sc_genre, sc_title, sc_artwork_url, sc_uri)


def save_result(genre, title, artwork, uri):
    playlist_exists = Popular.query.filter(Popular.url == uri).count()
    if not playlist_exists:
        new_playlist = Popular(title=title, genre=genre, pic=artwork, url=uri)
        db.session.add(new_playlist)
        db.session.commit()
