from selenium import webdriver

URL = 'https://ekel.kln.ac.lk/login/index.php'
# initialize browser
browser = webdriver.Chrome("chromedriver/chromedriver.exe")

# open browser with url
browser.get(URL)
# assert 'e-kelaniya: Log in to the site' in browser.title

browser.quit()

# download item from internet
# import requests

# url = "https://www106.zippyshare.com/d/vhf92KvE/40921/DC%20Pride%202022%20001%20%282022%29%20%28digital%29%20%28Son%20of%20Ultron-Empire%29.cbr"
# r = requests.get(url, allow_redirects=True)
# open('dc pride 2022.zip', 'wb').write(r.content)

# import wget
# r = wget.download(url, "dc pride 2022.cbr")

# import os
# os.rename("dc pride 2022.cbr", "dc pride 2022.rar")
# files = os.listdir()
# for file in files:
#     if file == "dc pride 2022.cbr":
#         pass

#extract files
# import zipfile
# with zipfile.ZipFile("dc pride 2022.zip", 'r') as zip_ref:
#     zip_ref.extractall("dc pride 2022")


