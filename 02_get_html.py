from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# Get the HTML
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url = 'https://www.classcentral.com'



def scrap_webage(url):
  r = requests.get(url, headers = headers).text
  soup = BeautifulSoup(r, 'html.parser')
  return soup



soup = scrap_webage(url)
print(soup)
with open("index.html", "wb") as f:
   f.write(soup.encode('utf-8'))