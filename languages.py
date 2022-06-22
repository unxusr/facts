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
        #print(languages)
        for language in languages['related']:
            key = language['@id'].split('/')[-2]
            value = language['@id'].split('/')[-1]
            weight = language['weight']
            #related[key] = key
            # if weight <= 1 and weight >= 0.95:
            #     print(key, value, weight)
                #print(related)
            if key in l.keys() and weight <= 1 and weight >= 0.95:
                #print(language['@id'].split('/')[-1], language['weight'])
                #print(l[language['@id'].split('/')[-2]], f":{language['weight']}:", [language['@id'].split('/')[-1]], f"Is related to {word}")
                related[l[language['@id'].split('/')[-2]]] = [language['weight'], value]

                #if key not in related:
                #     related[l[key]] = value
                # elif isinstance(related[key], list):
                #     related[key].append(value)
                # else:
                #     related[key] = value
        #for keys, values in related.items():
            #print(keys, '-', values)

    print(related)
    return related


w = sys.argv[1]
langs(w)
