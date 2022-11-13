import requests, os
from bs4 import BeautifulSoup

MODEL_PAGE_URL = "https://yostagram.com/tag/viking-barbie-instagram/"


def get_pages(page:str, page_links:list):
    response = requests.get(page)
    soup = BeautifulSoup(response.content,features="html.parser")
    pages = soup.find_all(name='a', class_="read-more")
    for page_link in pages:
        page_links.append(page_link.get("href"))
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
        return


def get_image_link(image_page:str):
    response = requests.get(image_page)
    soup = BeautifulSoup(response.content,features="html.parser")
    page = soup.find(name='a', class_="wp-block-button__link wp-element-button", string="Download")
    image_url = page.get("href")
    image_name = image_url[image_url.rfind("/")+1:]
    
    #save image
    r = requests.get(image_url, allow_redirects=True)
    open(image_name, 'wb').write(r.content)


def make_folder_for_downloads(main_url:str):
    # main_url == MODEL_PAGE_URL
    folder_name = main_url[main_url.removesuffix("/").rfind("/")+1:].removesuffix("-instagram/").replace("-", " ")
    if not os.path.exists(folder_name):
        os.makedirs(f"./{folder_name}")

# img_pages = []
# get_pages(MODEL_PAGE_URL, img_pages)
# print(len(img_pages))
# print(img_pages[0])
# get_image_link("https://yostagram.com/viking-barbie-instagram-319/")
# make_folder_for_downloads(MODEL_PAGE_URL)