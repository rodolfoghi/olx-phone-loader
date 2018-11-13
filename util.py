from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_site_html(url):
    try:
        html = urlopen(url)
        return html
    except HTTPError as e:
        print(e)
        return None

def get_bsobj_from(html):
    try:
        bs_obj = BeautifulSoup(html.read(), "html.parser")
        return bs_obj
    except AttributeError as e:
        print(e)
        return None