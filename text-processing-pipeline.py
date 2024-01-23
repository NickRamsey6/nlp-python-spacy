# Following along with chapter 2
import spacy
# Need to run $ python -m spacy download en in terminal
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'this product integrates both libraries for downloading and applying patches')
for token in doc:
    print(token.text, token.lemma_)
