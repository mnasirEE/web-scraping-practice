import requests

from bs4 import BeautifulSoup

with open ("html_doc.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.text)
# print(soup.prettify)
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id= 'link2'))

# extracting url from website
# for link in soup.find_all('a'):
#     print(link.get("href"))

# Another common task is extracting all the text from a page:

# print(soup.get_text())

print(soup.select('div.itallic'))
print(soup.select("a#link2"))

