import requests, logging
from config import Config
from datetime import datetime
from webapp.parsing.utils import get_html, save_bandcamp


logger = logging.getLogger(__name__)

def bandcamp_parsing():
    bandcamp_urls = Config.BC_API
    for urls in bandcamp_urls:
        html = get_html(urls)
        if html:
            try:
                for info in html['items'][:4]:
                    genre = info['genre_text'] #genre
                    art = info['art_id'] #art number (для получения картинки в дальнейшем)
                    #primary_text = info['primary_text'] #album name
                    author = info['secondary_text'] #author name
                    title = info['featured_track']['title'] #song name
                    music_url = info['featured_track']['file']['mp3-128'] #song    
                    date_entry = datetime.now()
                    save_bandcamp(genre, art, author, title, music_url, date_entry)                
            except (KeyError, ValueError) as error:
                logger.error(error)
                'Ошибка при подключении к Bandcamp'
