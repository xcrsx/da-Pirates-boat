import requests
from webapp.search.forms import MusicSearchForm


def search_sc():
    form = MusicSearchForm()
    url = 'https://api-v2.soundcloud.com/search?'
    data = {
        'q': form.search.data,
        'sc_a_id': '3f437705c7fa502c1d352917a83b95768acbe00a',
        'variant_ids': '',
        'facet': 'model',
        'user_id': '57289-61909-388511-64921',
        'client_id': '9yZSvlXAK7Wmu4xhb0hdMtjP9D2z351X',
    }
    r = requests.get(url, data)
    r = r.json()
    search_result = []
    for result in r['collection']:
        url_song = result['permalink_url']
        search_result.append({'song': url_song})
    return search_result
