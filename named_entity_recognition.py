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
    return f"Found dates: {dates}", f"Found Cardinals: {cardinals}"



# Salah PERSON
# 2 CARDINAL
# 2020 DATE
# Google ORG

sent = "Salah went to Maldives 2 times in June 2020 and Google 3rd of August recorded that "
#sent = "Apple is looking at buying U.K. startup for $1 billion"
#sent = sys.argv[1]
#sys.stdin[1]
get_dates_cardinals(sent)
