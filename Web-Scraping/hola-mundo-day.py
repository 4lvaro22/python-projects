from bs4 import BeautifulSoup
import os
import requests

_url = "https://holamundo.day/"
request = requests.get(_url).content

soup = BeautifulSoup(request)

blockquotes = soup.find_all('blockquote')

print(os.getcwd())

f = open("./Web Scraping/Day-8-event.txt", "w")
for blockquote in blockquotes[21:]:
    f.write(blockquote.text + "\n")

