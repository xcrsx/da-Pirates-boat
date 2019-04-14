import requests
from config import Config
from webapp.models import Bandcamp
from webapp.models import db

def bandcamp_parsing():
    bandcamp_url = Config.BC_API
    bc_result = []    
    for url in bandcamp_url:
        try:
            result = requests.get(url)
            result = result.json()                  
            for info in result['items'][:8]:
                genre_text = info['genre_text'] #genre
                art_id = info['art_id'] #art number (для получения картинки в дальнейшем)
                primary_text = info['primary_text'] #album name
                secondary_text = info['secondary_text'] #autor name
                title = info['featured_track']['title'] #song name
                file = info['featured_track']['file']['mp3-128'] #song    
                #publish_date = info['publish_date']            
                bc_result.append({
                    'genre_text': genre_text,
                    'art_id': art_id,
                    'primary_text': primary_text,
                    'secondary_text': secondary_text,
                    'title': title,
                    'file': file,
                })
            return bc_result
        except (KeyError, ValueError):
            'Ошибка при подключении к Bandcamp'   
    save_result(genre_text, art_id, primary_text, secondary_text, title, file)


def save_result(genre_text, art_id, primary_text, secondary_text, title, file):
    playlist_exists = Bandcamp.query.filter(Bandcamp.file == file).count()
    if not playlist_exists:
        new_playlist = Bandcamp(genre_text=genre_text, 
                            art_id=art_id, 
                            primary_text=primary_text, 
                            secondary_text=secondary_text,
                            title=title,
                            file=file)
        db.session.add(new_playlist)
        db.session.commit()
