import pycountry
import sys
from tokenizer import tokenize


def get_currency(phrase):
    for token in tokenize(phrase):
        for country in pycountry.countries:
            if country.name.lower() in phrase.lower():
                nu = pycountry.countries.get(numeric=country.numeric)
                for currency in pycountry.currencies:
                    if currency.numeric == country.numeric:
                        return f"Currency for {country.name} is:", pycountry.currencies.get(numeric=str(nu.numeric)).name
                    elif country.name.lower() == token.capitalize():
                        return pycountry.currencies.lookup(token)


txt = sys.argv[1]
print(get_currency(txt))
