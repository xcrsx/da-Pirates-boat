import requests



class SoundCloudParsing():
    soundcload_main_url = "https://api-v2.soundcloud.com/selections?client_id=wQF3qEmVErE295tmLg8c1xxt5Y5kLda2&limit=10&offset=0&linked_partitioning=1&app_version=1552470605&app_locale=en"
    result = requests.get(soundcload_main_url)
    value = result.json()
    sc_result = []
    for info in value['collection']:
        try:
            sc_title = info['title']
            sc_playlist = info['playlists'][0]['permalink']
            sc_pic = info['playlists'][0]['artwork_url']
            sc_result.append({
                'title': sc_title,
                'playlist': sc_playlist,
                'pic': sc_pic,
            })
        except (KeyError):
            pass


 
 
