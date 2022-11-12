from urllib.request import urlopen

html_page = urlopen("http://daftsex.com/").read().decode("utf-8")


print(html_page)