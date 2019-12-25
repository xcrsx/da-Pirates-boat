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
        'user_id': '364967-67608-407779-700571',
        'client_id': 'YUKXoArFcqrlQn9tfNHvvyfnDISj04zk',
    }
    # limit=20&offset=0&linked_partitioning=1&app_version=1576752087&app_locale=en
    r = requests.get(url, data)
    search_result = []
    r = r.json()
    for result in r['collection']:
        url_song = result['permalink_url']
        search_result.append({'song': url_song})
    return search_result
