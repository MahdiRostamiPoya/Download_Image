"""
download image from google with python -> Web Scraping

libraries:
    requests -> pip3 install requests
    bs4 -> pip3 install BeautifulSoup4

telegram channel:
    @MTQD_1400

telegram group:
    @MTQD_1400_Group

MahdiQD :)
"""

import requests
from requests import get, exceptions
from bs4 import BeautifulSoup

def search_download_image(text:str=None):
    url = f"https://www.google.com/search?q={text}&source=lnms&tbm=isch"
    try:
        res = get(url)
        if res.ok:
            soup = BeautifulSoup(res.text, "html.parser")
            images = soup.find_all("img")
            count_download = int(input("How many photos should i download ? "))
            link_images = [img["src"] for img in images][1:count_download+1:]
            for count, url_img in enumerate(link_images):
                res = get(url_img)
                if res.ok:
                    with open(f"{count}.png", "wb") as f: f.write(res.content)
            print("successful !!")

    except exceptions.ConnectionError as connection_error:
        print(f"Connection Error\nError: {connection_error}")
    except exceptions.HTTPError as http_error:
        print(f"https error\nError: {http_error}")
    except exceptions.Timeout as timeout:
        print(f"Timeout Error\nError: {timeout}")

search_download_image("game")
