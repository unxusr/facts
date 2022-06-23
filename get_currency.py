import sys

import pycountry
from tokenizer import tokenize

import re

def pluralize(noun):
    if re.search('[sxz]$', noun):
         return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


def get_currency(phrase):
    for currency in pycountry.currencies:
        for token in tokenize(phrase):
            if token.upper() == currency.alpha_3:
                return currency.name
            elif token.capitalize() == currency.name:
                return currency.name
            elif token in pluralize(currency.name.lower()):
                return currency.name
            elif token in pluralize(currency.alpha_3.lower()):
                return currency.name
