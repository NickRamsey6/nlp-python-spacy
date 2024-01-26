# Chapter 4
import spacy
nlp = spacy.load("en_core_web_sm")

# Use scpacy.explain() to return a description of each given lingustic feature
# doc = nlp(u"The firm earned $1.5 million in 2017.")
# for token in doc:
#     print(token.text, token.pos_, spacy.explain(token.pos_))

# Print course-grained and fine-grained part-of-speech tags and explain fine-grained
doc = nlp(u"The firm earned $1.5 million in 2017.")
for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))
