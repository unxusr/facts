import nltk
from nltk.corpus import stopwords


def tokenizer(sent):
    tokens = nltk.word_tokenize(sent)
    english_stops = set(stopwords.words('english'))
    words = [w for w in tokens if not w in english_stops]
    return words


sent = "we need to go in a trip for fun and have some gifts"
tokenizer(sent)
