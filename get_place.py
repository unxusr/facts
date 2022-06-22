import pycountry
from geotext import GeoText

txt = "london is from france"
euro = pycountry.currencies.get(alpha_3='EUR')


def get_country(phrase):
    for c in pycountry.countries:
        if c.name.lower() in phrase:
            print(c.name)
            #print(c.alpha_2)
            print(pycountry.countries.get(alpha_2=c.alpha_2))
            #print(c.official_name)
            return f"Found Countries: {c.name}"


#get_city(txt)
get_country(txt)
