from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request('https://daftsex.com/playlist/187449/100017', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req).read()

soup = BeautifulSoup(html_page, 'html.parser')
links = []
# print(soup)
with open("twitter.html", "w", encoding="utf-8") as file:
    file.write(soup.text)
# for link in soup.findAll('a', attrs={'href': re.compile("^/movie/")}):
#     links.append(link.get('href'))
#
# print(links)
