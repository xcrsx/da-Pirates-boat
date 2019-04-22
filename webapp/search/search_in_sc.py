import requests
from webapp.search.forms import MusicSearchForm


def search_sc():
    form = MusicSearchForm()
    r = requests.get('https://api-v2.soundcloud.com/search?q=' +
                     form.search.data +
                     '&sc_a_id=3f437705c7fa502c1d352917a83b95768acbe00a&variant_ids=&facet=model&user_id=57289-61909-388511-64921&client_id=9yZSvlXAK7Wmu4xhb0hdMtjP9D2z351X&limit=20&offset=0&linked_partitioning=1&app_version=1553857576&app_locale=en')
    r = r.json()
    search_result = []
    for result in r['collection']:
        url_song = result['permalink_url']
        search_result.append({'song': url_song})
    return search_result
