import requests
import json
proxies = {'https': 'https://143.208.200.26:7878',
         'http': 'http://143.208.200.26:7878'}

def fetch_data(url, path):
    r= requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://www.codewithharry.com/tutorial/js/"

fetch_data(url, "data/times.html")




