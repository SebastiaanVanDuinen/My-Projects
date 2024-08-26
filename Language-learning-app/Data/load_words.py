import requests
import json
from bs4 import BeautifulSoup

url_arabic_words = "https://blogs.transparent.com/arabic/learn-the-100-most-common-words-in-arabic/"
url_dutch_words = "https://www.pinhok.com/kb/dutch/146/100-basic-dutch-vocabularies/"
url_french_words = "https://www.languagebard.com/most-common-100-french-words"

def get_french_words():
    page = requests.get(url_french_words)
    html_page = BeautifulSoup(page.content, "html.parser")
    table = html_page.find(text="The List").find_next('ol')
    res = [['{}'.format(li.string)] for li in table.find_all('li')]
    return res

def get_dutch_words():
    page = requests.get(url_dutch_words)
    html_page = BeautifulSoup(page.content, "lxml")
    table = html_page.find('table')
    table_rows = table.find_all('tr')

    res = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip().replace(" in Dutch", "") for tr in td if tr.text.strip()]
        if row:
            res.append(row)
    with open("DU_top100.json", "w") as data_file:
        json.dump(res, data_file)
    return res


def get_arab_words():
    page = requests.get(url_arabic_words)
    html_page = BeautifulSoup(page.content, "lxml")

    table = html_page.find('table')
    table_rows = table.find_all('tr')

    res = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)
    fixed_res = [(b, c) for (a, b, c) in res]

    with open("AR_top100.json", "w") as data_file:
        json.dump(fixed_res, data_file)
    return fixed_res


data = get_french_words()
print(data)