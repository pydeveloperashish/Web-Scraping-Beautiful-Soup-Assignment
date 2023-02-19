from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import pandas as pd
import numpy as np

s = HTMLSession()


# Get the HTML
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url = 'https://www.classcentral.com'



def getdata(url):
  r = s.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup

  
soup = getdata(url)
with open("text.txt", "w") as f:
  f.write(soup.get_text())
