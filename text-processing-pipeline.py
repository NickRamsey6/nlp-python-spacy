# Following along with chapter 2
# Had to downgrade to Spacy 2.3.5 b/c they recently changed tokenizer exceptions to ORTH and NORM
import spacy
# Need to run $ python -m spacy download en in terminal
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I have flown to LA. Now I am flying to Frisco')
print([w.text for w in doc if w.tag_ == 'VBG' or w.tag_ =='VB'])
print([w.text for w in doc if w.pos_ == 'PROPN'])

