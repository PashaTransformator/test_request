# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

def get_url(href):
    r = requests.get(href)
    print(r.text)

href = 'https://khashtamov.com/ru/pandas-introduction/'

get_url(href)
