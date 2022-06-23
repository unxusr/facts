import requests
import sentiment
from tokenizer import tokenize
import google_query
from check_colors import check_color
from get_currency import get_currency
from named_entity_recognition import get_dates_cardinals
from get_city import get_geo_place
from languages import langs
from facts import facts
import json


def brain(phrase):
    fact = facts(phrase)
    senti = sentiment.get_sentiments(phrase)
    google_result = google_query.search(phrase)
    city = get_geo_place(phrase)
    color = [i for i in tokenize(phrase) if check_color(i)]
    currency = get_currency(phrase)
    numeric = get_dates_cardinals(phrase)
    lang = langs(phrase)

    return {"Facts": fact, "Sentiment": senti, "Google_result": google_result,
            "Location": city, "Colors": color, "Currencies": currency,
            "Cardinals": numeric, "Languages": lang}


