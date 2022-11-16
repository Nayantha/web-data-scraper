import os
import shutil

import requests
from bs4 import BeautifulSoup

def make_model_tag_urls(model_name:str):
    model_name = model_name.lower().strip().replace(" ", "-")
    url = f"https://yostagram.com/tag/{model_name}-instagram/"
    req = requests.get(url=url)
    if req.status_code != 200:
        print(f"{model_name} not exit on yostagram or name is in wrong format.")
    else:
        return url

def get_all_models_from_site_map():
    URL = "https://yostagram.com/site-map/"
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, features="html.parser")
    model_links = [item.get("href").replace("/tag/","").replace("-instagram/", "") for item in soup.find_all(name='a') if "instagram" in item.get("href")]
    return model_links

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
        return page_links.copy()

def get_image_link_and_name(image_page:str):
    response = requests.get(image_page)
    soup = BeautifulSoup(response.content,features="html.parser")
    page = soup.find(name='a', class_="wp-block-button__link", string="Download")
    image_url = page.get("href")
    image_name = image_url[image_url.rfind("/")+1:] 
    print(f"got {image_name}'s url at {image_url}")
    return {"image_name": image_name, "image_url": image_url}
    
def save_image(path:str, image_name:str, image_url:str):
    r = requests.get(image_url, allow_redirects=True)
    if path.rfind('/') == len(path) - 1:
        path = path.removesuffix("/")
    open(f"{path}/{image_name}", 'wb').write(r.content)
    print(f"{image_name} saved in {path}")

def get_folder_name(url:str):
    return url[url.removesuffix("/").rfind("/")+1:].removesuffix("-instagram/").replace("-", " ").title()

def make_folder_for_downloads(folder_name:str):
    if not os.path.exists(folder_name):
        os.makedirs(f"./{folder_name}")

def is_image_already_exists(path:str, file_name:str):
    files = os.listdir(path=path)
    for file in files:
        if file == file_name : #or file_name in file:
            return True
    return False

def download_images_from_yostagram(model_page_link:str):
    img_pages = []
    img_data_list = []
    path = "./models"
    folder_name = get_folder_name(model_page_link)
    get_pages(model_page_link, img_pages)
    for image_page in img_pages:
        img_data_list.append(get_image_link_and_name(image_page))
    print("All image links are retrieved.")
    print("Makeing place for downloads...")
    make_folder_for_downloads(path)
    path += f"/{folder_name}"
    make_folder_for_downloads(path)
    for img_data_item in img_data_list:
        img_name =  img_data_item["image_name"]
        if not is_image_already_exists(path, img_name):
            img_url =  img_data_item["image_url"]
            save_image(path=path, image_name=img_name, image_url=img_url)
        else:
            print(f"{img_name} is already exists.")

def make_file_cbz(path:str):
    if path.rfind("/") == len(path) - 1:
        path += "/"
    output = path
    # dir_name = path
    try:
        make_folder_for_downloads("zip files")
        zip_name = shutil.make_archive(output, "zip", path)
        os.rename(zip_name, zip_name.replace(".zip", ".cbz"))
    except Exception:
        print("error")

def archive_all_folders(path:str):
    folders =  [file for file in os.listdir(path=path) if os.path.isdir(file)]
    print(folders)

if __name__ == "__main__":
    model_names = get_all_models_from_site_map()
    model_urls = [ make_model_tag_urls(model_name) for model_name in model_names]
    for model_url in model_urls:
        print(model_names[model_urls.index(model_url)])
        download_images_from_yostagram(model_url)
        
    
