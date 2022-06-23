import spacy


def get_dates_cardinals(sent):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sent)
    cardinals = []
    dates = []
    for ent in doc.ents:
        if ent.label_ == "CARDINAL":
            cardinals.append(ent)
        if ent.label_ == "DATE":
            dates.append(ent)
    return f"dates: {dates}", f"Cardinals: {cardinals}"
