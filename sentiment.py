import requests
import sys


def get_sentiments(phrase):
    url = f"http://text-processing.com/api/sentiment/"
    body = f"text={phrase}"
    label = ""
    response = requests.post(url, data=body)
    if response.json()['label'] == "pos":
        label = "Positive"
    elif response.json()['label'] == "neg":
        label = "Negative"
    elif response.json()['label'] == "neutral":
        label = "Neutral"
    return f"Your phrase was:-> {phrase}.", f"Sentiment:-> {label}"


# word = sys.argv[1]
# get_sentiments(word)
