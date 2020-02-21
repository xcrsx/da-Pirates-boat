import requests
from webapp.search.forms import MusicSearchForm
from config import Config
from webapp.parsing.utils import create_url
import logging


logger = logging.getLogger(__name__)


def search_sc():
    form = MusicSearchForm()
    task = form.search.data
    url = create_url("https://api-v2.soundcloud.com/search?q=", task)
    try:
        r = requests.get(url)
        search_result = []
        r = r.json()
        for result in r['collection']:
            url_song = result['permalink_url']
            search_result.append({'song': url_song})
        return search_result
    except Exception as error:
        logger.error(error)
        print("Ошибка поиска. Смотреть лог файл")
        return
