import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Connection error")
        return False

def get_daily_music():
    html = get_html("https://daily.bandcamp.com")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        daily_music = soup.find('div', id='content').findAll('iframe')
        result_music = []
        for music in daily_music:
            url = music.get('src')
            result_music.append({
                'url': url
            })
        return result_music
    return False
