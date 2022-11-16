import requests
from bs4 import BeautifulSoup

res = requests.get("https://twitter.com/yarishna_ayala").content

soup = BeautifulSoup(res, features="html.parser")

links = soup.find_all(name="a")
for link in links:
    print(link)