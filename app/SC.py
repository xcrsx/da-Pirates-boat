import requests
from app.models import Popular
from app import db


class SoundCloudParsing():
    soundcload_main_url = "https://api-v2.soundcloud.com/selections?client_id=wQF3qEmVErE295tmLg8c1xxt5Y5kLda2&limit=10&offset=0&linked_partitioning=1&app_version=1552470605&app_locale=en"
    result = requests.get(soundcload_main_url)
    value = result.json()
    sc_result = []
    for info in value['collection']:
        try:
            sc_title = info['title']
            sc_playlist = info['playlists'][0]['title']
            sc_player = info['playlists'][0]['permalink_url']
            if info['playlists'][0]['artwork_url'] is None:
                sc_pic = info['playlists'][0]['user']['avatar_url']
            else:
                sc_pic = info['playlists'][0]['artwork_url']
            sc_result.append({
                'title': sc_title,
                'playlist': sc_playlist,
                'player': sc_player,
                'pic': sc_pic,
            })
        except (KeyError):
            pass


'''def save_popular(title, genre, pic, url):
    playlist_exists = Popular.query.filter(Popular.url == url).count()
    if not playlist_exists:
        new_playlist = Popular(title=title, genre=genre, pic=pic, url=url)
        db.session.add(new_playlist)
        db.session.commit()'''
