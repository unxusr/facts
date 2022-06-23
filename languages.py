import sys
import requests
from tokenizer import tokenize
import numpy as np


def langs(query):
    words = tokenize(query)
    l = {'en': 'English', 'fr':'French', 'de': 'German',
         'ja': 'Japanese', 'zh': 'Chinese', 'ur': 'Urdu',
         'it': 'Italian', 'es': 'Spanish', 'ru': 'Russian',
         'pt': 'Portuguese', 'nl': 'Dutch', 'ar': "Arabic"}
    related = {}
    for word in words:
        languages = requests.get(f'https://api.conceptnet.io/related/c/en/{word}?limit=1000').json()
        for language in languages['related']:
            key = language['@id'].split('/')[-2]
            value = language['@id'].split('/')[-1]
            weight = language['weight']
            if key in l.keys() and weight <= 1 and weight >= 0.95:
                related[l[language['@id'].split('/')[-2]]] = [language['weight'], value]

    return related
