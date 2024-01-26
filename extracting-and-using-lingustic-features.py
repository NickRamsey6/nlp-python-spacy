# Chapter 4
import spacy
nlp = spacy.load("en_core_web_sm")

# Use scpacy.explain() to return a description of each given lingustic feature
doc = nlp(u"The firm earned $1.5 million in 2017.")
for token in doc:
    print(token.text, token.pos_, spacy.explain(token.pos_))

# Print course-grained and fine-grained part-of-speech tags and explain fine-grained
doc = nlp(u"The firm earned $1.5 million in 2017.")
for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))

# Use part of speech tags to find $1.5 million but not 2017
doc = nlp(u"The firm earned $1.5 million in 2017.")
phrase = ''
for token in doc:
    if token.tag_ == '$':
        phrase = token.text
        i = token.i+1
        while doc[i].tag_ == 'CD':
            phrase += doc[i].text + ' '
            i+=1
        break
phrase = phrase[:-1]
print(phrase)

# Turn statement into question
doc = nlp(u"I can promise it is worth your time.")
sent = ''
for i, token in enumerate(doc):
    if token.tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
        sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
        sent = sent + ' ' + doc[i+2:].text
        break
# Retokenization
doc = nlp(sent)
for i, token in enumerate(doc):
    if token.tag_ == 'PRP' and token.text == 'I':
        sent = doc[:i].text + ' you ' + doc[i+1:].text
        break
doc = nlp(sent)
for i, token in enumerate(doc):
    if token.tag_ == 'PRP$' and token.text == 'your':
        sent = doc[:i].text + ' my ' + doc[i+1:].text
        break
doc = nlp(sent)
for i, token in enumerate(doc):
    if token.tag_ == 'VB':
        sent = doc[:i].text + ' really ' + doc[i:].text
        break
doc = nlp(sent)
sent = doc[:len(doc)-1].text + '?'
print(sent)