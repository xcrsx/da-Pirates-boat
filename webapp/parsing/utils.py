import requests
from webapp.db import db
from webapp.parsing.models import Bandcamp, SoundCloud

def get_html(url):
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
		}
		result = requests.get(url, headers=headers)
		result.raise_for_status()
		return result.json()
	except(requests.RequestException, ValueError):
		print('Сетевая ошибка')
		return False


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