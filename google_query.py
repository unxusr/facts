import json
import requests
import re
import settings
import sys


def remove_dates(sentence):
    sentence = re.sub('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1}|,|\s\d{4}', '', sentence)
    return sentence


def search(query):
    api_key = settings.api_key
    search_engine_id = settings.search_engine_id
    url = "https://customsearch.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s" % (api_key, search_engine_id, query)
    result = requests.Session().get(url)
    rjson = json.loads(result.content)
    try:
        result = remove_dates(rjson['items'][0]['snippet'])
    except:
        return "No Information Available"
    return result
