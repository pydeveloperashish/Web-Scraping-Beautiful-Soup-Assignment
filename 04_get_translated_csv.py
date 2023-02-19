import pandas as pd
import os
from tqdm.auto import tqdm
from googletrans import Translator
translator = Translator()

df = pd.read_csv('to_translate.csv')


translated_text_hindi_list = []
for value in tqdm(df['English']):
    translated_text_hindi = translator.translate(value, dest = 'hi').text
    translated_text_hindi_list.append(translated_text_hindi)


df['Hindi'] = translated_text_hindi_list

df.to_csv('translated.csv', index = False)

