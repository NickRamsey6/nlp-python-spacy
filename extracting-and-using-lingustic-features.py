# Chapter 4
import spacy
nlp = spacy.load("en_core_web_sm")

# Use scpacy.explain() to return a description of each given lingustic feature
doc = nlp(u"The firm earned $1.5 million in 2017.")
for token in doc:
    print(token.text, token.pos_, spacy.explain(token.pos_))
