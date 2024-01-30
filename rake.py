import nltk 
# nltk.download('punkt')
# nltk.download('stopwords')
from requests_html import HTMLSession
from rake_nltk import Rake

def extract_text():
    s = HTMLSession()
    url = 'https://www.musicradar.com/reviews/tech/akg-c214-172209'
    response = s.get(url)
    return response.html.find('div#article-body', first=True).text

print(extract_text())