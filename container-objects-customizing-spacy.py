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

# Check last word in sentence for verb. Reduce length of sentence by 2 to account for punctuation mark.
doc = nlp(u'A severe storm hit the beach. It started to rain.')
counter = 0
for sent in doc.sents:
    if sent[len(sent)-2].pos_=='VERB':
        counter+=1
print(counter)

# Access noun_chunks container
doc = nlp(u'A noun chunk is a phrase that has a noun as its head.')
for chunk in doc.noun_chunks:
    print(chunk)

# Manually find noun_chunks. Iterate over tokens and grab only nouns, iterate over noun's children and only grab determiners or adjectives then append
doc = nlp(u'A noun chunk is a phrase that has a noun as its head.')
for token in doc:
    if token.pos_=='NOUN':
        chunk=''
        for w in token.children:
            if w.pos_=='DET' or w.pos_=='ADJ':
                chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)
# Option 2: use lefts instead of children because words that modify a noun are always leftward syntactic children of the noun
for token in doc:
    if token.pos_=='NOUN':
        chunk=''
        for w in token.lefts:
            chunk =  chunk + w.text+ ' '
        chunk = chunk + token.text
        print(chunk)