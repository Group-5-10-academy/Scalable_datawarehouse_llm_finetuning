from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import random 
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import sys
import re
from nltk import BigramCollocationFinder
import nltk.collocations 

def data_scrap(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    texts = soup.find_all('div', class_='bbc-19j92fr ebmt73l0')
    
    # Initialize an empty list to collect paragraph texts
    article_paragraphs = []
    
    for text in texts:
        paragraphs = text.find_all('p', class_='bbc-1f7v08l e17g058b0')
        for paragraph in paragraphs:
            article_paragraphs.append(paragraph.text)
    
    # Join all paragraphs into a single string with double newlines between paragraphs
    article = '\n\n'.join(article_paragraphs)
    return article

url = 'https://www.bbc.com/amharic/articles/c9771yrrv77o'
article = data_scrap(url)
print(article)
