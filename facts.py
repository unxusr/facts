import requests
import sentiment
from tokenizer import tokenize
import google_query
from check_colors import check_color
from get_currency import get_currency
from named_entity_recognition import get_dates_cardinals
from get_city import get_geo_place
from languages import langs


def facts(word):
    print("getting facts...")
    data = []
    if len(word.split()) >= 1:
        words = tokenize(word)
        for word in words:
            partof = requests.get(f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/PartOf&limit=5').json()
            for i in range(len(partof['edges'])):
                if partof['edges'][i]['surfaceText'] is not None:
                    clean = partof['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)
                else:
                    print("Concept Net is Down!")

            usedfor = requests.get(f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/UsedFor&limit=1').json()
            for i in range(len(usedfor['edges'])):
                if usedfor['edges'][i]['surfaceText'] is not None:
                    clean = usedfor['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)
                else:
                    print("Concept Net is Down!")

            relatedto = requests.get(
                f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/RelatedTo&limit=5').json()
            for i in range(len(relatedto['edges'])):
                if relatedto['edges'][i]['surfaceText'] is not None:
                    clean = relatedto['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)
                else:
                    print("Concept Net is Down!")

    return data
