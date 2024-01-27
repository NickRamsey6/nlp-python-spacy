import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS

# Load text file
with open('hound.txt') as infile:
    text = infile.read()

# Load image as numpy array
