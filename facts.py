import requests
import sentiment
import tokenizer
import gquery


def facts(word):
    print("getting facts...")
    data = []
    senti = sentiment.get_sentiments(word)
    google_result = gquery.search(word)
    if len(word.split()) >= 1:
        words = tokenizer.tokenizer(word)
        for word in words:
            partof = requests.get(f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/PartOf&limit=5').json()
            for i in range(len(partof['edges'])):
                if partof['edges'][i]['surfaceText'] is not None:
                    clean = partof['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)

            usedfor = requests.get(f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/UsedFor&limit=5').json()
            for i in range(len(usedfor['edges'])):
                if usedfor['edges'][i]['surfaceText'] is not None:
                    clean = usedfor['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)

            relatedto = requests.get(f'http://api.conceptnet.io/query?node=/c/en/{word}&rel=/r/RelatedTo&limit=5').json()
            for i in range(len(relatedto['edges'])):
                if relatedto['edges'][i]['surfaceText'] is not None:
                    clean = relatedto['edges'][i]['surfaceText'].replace('[[', '')
                    clean = clean.replace(']]', '')
                    data.append(clean)
    return senti, google_result, data
