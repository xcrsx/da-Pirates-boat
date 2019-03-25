import requests
from config import Config


class SoundCloudParsing():
    soundcload_main_url = Config.SC_API_MAINPAGE
    result = requests.get(soundcload_main_url)
    value = result.json()
    sc_result = []
    for info in value['collection']:
        try:            
            if info['genre'] is "":
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
                'uri': sc_uri,
            })
        except (KeyError, ValueError):
            'Ошибка при подключении к главной странице SoundCloud'
