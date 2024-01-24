# Chapter 3
import spacy
from spacy.tokens.doc import Doc
from spacy.vocab import Vocab
nlp = spacy.load("en_core_web_sm")

# Obtain all leftward syntactic children of word at position 4
doc = nlp(u'I want a green apple.')
print([w for w in doc[4].lefts])