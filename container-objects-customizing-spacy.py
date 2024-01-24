# Chapter 3
import spacy
from spacy.tokens.doc import Doc
from spacy.vocab import Vocab
nlp = spacy.load("en_core_web_sm")

# Obtain all leftward syntactic children of word at position 4
doc = nlp(u'I want a green apple.')
print([w for w in doc[4].lefts])
# Could also use [w for w in doc[4].children] to get all children

# Separate text into sentences and return all tokens in each individual sentence
doc = nlp(u'A severe storm hit the beach. It started to rain.')
for sent in doc.sents:
    print([sent[i] for i in range(len(sent))])

# Check if second sentence begins with a pronoun
doc = nlp(u'A severe storm hit the beach. It started to rain.')
for i, sent in enumerate(doc.sents):
    if i==1 and sent[0].pos_=='PRON':
        print('The second sentence begins with a pronoun.')

# Check last word in sentence for verb
doc = nlp(u'A severe storm hit the beach. It started to rain.')
counter = 0
for sent in doc.sents:
    if sent[len(sent)-2].pos_=='VERB':
        counter+=1
print(counter)
