import requests, logging
from config import Config
from datetime import datetime
from webapp.parsing.utils import get_html, save_soundcloud


logger = logging.getLogger(__name__)

def soundcloud_parsing():
    html = get_html(Config.SC_API_MAINPAGE)
    if html:
        try:
            for info in html['collection']:
                genre = info['genre']
                if info['artwork_url'] == None:
                    art = info['user']['avatar_url']
                else:
                    art = info['artwork_url']
                author = info['user']['username']
                title = info['title']
                music_url = info['uri']
                date_entry = datetime.now()
                save_soundcloud(genre, art, author, title, music_url, date_entry)
        except (KeyError ,ValueError) as error:
            lohher.error(error)
            'Ошибка при подключении к Sound Cloud'