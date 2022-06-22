from geotext import GeoText
from tokenizer import tokenize


def get_geo_place(word):
    city = []
    country = []
    words = tokenize(word)
    for word in words:
        if GeoText(word.capitalize()).cities:
            city.append(word.capitalize())
        if GeoText(word.capitalize()).countries:
            country.append(word.capitalize())
    print(f"Cities: {city}", f"Countries: {country}")
    return f"Cities: {city}", f"Countries: {country}"


get_geo_place("paris is the capital of france")