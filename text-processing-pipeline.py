# Following along with chapter 2
# Had to downgrade to Spacy 2.3.5 b/c they recently changed tokenizer exceptions to ORTH and NORM
import spacy
# Need to run $ python -m spacy download en in terminal
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I have flown to LA. Now I am flying to Frisco')
for sent in doc.sents:
    print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])

