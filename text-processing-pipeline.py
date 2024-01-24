# Following along with chapter 2
# Had to downgrade to Spacy 2.3.5 b/c they recently changed tokenizer exceptions to ORTH and NORM
import spacy
# Need to run $ python -m spacy download en in terminal
from spacy.symbols import ORTH, LEMMA
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I have flown to LA. Now I am flying to Frisco')
special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
print([w.lemma_ for w in nlp(u'I have flown to LA. Now I am flying to Frisco') if w.dep_=='ROOT' and w.tag_=='VBG' or w.dep_=='pobj' and ((w.head).head).tag_=='VBG'])
