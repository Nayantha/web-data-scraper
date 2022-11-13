import requests
from bs4 import BeautifulSoup

MODEL_PAGE_URL = "https://yostagram.com/tag/viking-barbie-instagram/"


def get_pages(page:str, page_links:list):
    response = requests.get(page)
    soup = BeautifulSoup(response.content,features="html.parser")
    pages = soup.find_all(name='a', class_="read-more")
    for page_link in pages:
        page_links.append(page_link)
    if "/page/" not in page:
        print("page 01 is done....")
    else :
        page_no = int(page[page.rfind('e/')+2:-1])
        if page_no < 10:
            page_no = f"0{page_no}"
        print(f"page {page_no} is done...")
    try :
        next_page = soup.find(name='a', class_="next page-numbers").get("href")
        get_pages(next_page, page_links)
    except AttributeError:
        exit()


pages_ = []
get_pages(MODEL_PAGE_URL, pages_)

# for page in pages_:
#     print(page)

print(len(pages_))