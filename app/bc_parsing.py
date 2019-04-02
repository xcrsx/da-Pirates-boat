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
            allowtransparency = music.get('allowtransparency')
            frameborder = music.get('frameborder')
            height = music.get('height')
            src = music.get('src')
            style = music.get('style')
            width = music.get('width')
            result_music.append({
                'allowtransparency': allowtransparency,
                'frameborder': frameborder,
                'height': height,
                'src': src,
                'style': style,
                'width': width
                })
        return result_music
    return False
