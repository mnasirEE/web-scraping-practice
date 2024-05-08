import requests

from bs4 import BeautifulSoup

def fetch_data(path,url):
    r= requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url = "https://www.azbar.org/for-lawyers/practice-tools-management/member-directory/"
# fetch_data("arizon.html", url)

with open("arizon.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser") 
# print(soup.title)   
# row = soup.select("div.row")
# row = str(row)
# with open("t.html", "w") as f:
#     f.write(row)

# print(soup.select("div#divResultsAttorney"))
# print(soup.div.get('class'))

# print(soup.find(class_ = 'row'))

a = soup.find(id='divResultsAttorney')
print(a)
