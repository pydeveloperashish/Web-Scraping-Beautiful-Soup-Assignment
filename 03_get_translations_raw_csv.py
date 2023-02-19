from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import numpy as np


with open("text.txt", "r") as f:
  eng_text = ''.join(f.readlines()).split('\n')
  #eng_text = ' '.join(eng_text).split(' ')
  print(eng_text)
  
  
data = {
  "English": eng_text,
  "Hindi": "None"
}  

df = pd.DataFrame(data)
df['English'] = df['English'].replace('', np.nan)
df.dropna(axis = 0, inplace = True)
print(df.isna().sum())

df.to_csv('to_translate.csv')