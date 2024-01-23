# Following along with chapter 2
import spacy
from spacy.symbols import ORTH, LEMMA
# Need to run $ python -m spacy download en in terminal
# Had to downgrade to Spacy 2.3.5 b/c they recently changed tokenizer exceptions to ORTH and NORM
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])
special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
print([w.lemma_ for w in nlp(u'I am flying to Frisco')])
