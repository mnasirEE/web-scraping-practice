import requests
import json
proxies = {'https': 'https://143.208.200.26:7878',
         'http': 'http://143.208.200.26:7878'}


with requests.Session() as session:
    session.proxies = PROXY
    r = requests.get('http://ip-api.com/json')
    print(json.dumps(r.json(), indent=2))