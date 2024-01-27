import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS

# Load text file
with open('hound.txt') as infile:
    text = infile.read()

# Load image as numpy array
mask = np.array(Image.open('holmes.png'))

# Get stop words as a set and add extra words
stopwords = STOPWORDS
stopwords.update(['us', 'one', 'will', 'said', 'now', 'well',
                  'man', 'may', 'little', 'say', 'must', 'way',
                  'long', 'yet', 'mean', 'put', 'seem', 'asked',
                  'made', 'half', 'much', 'certainly', 'might', 'came'])
