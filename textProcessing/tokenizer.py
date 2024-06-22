import nltk
from nltk.tokenize import word_tokenize

def tokenizeText(text):
    tokens = word_tokenize(text)
    return tokens
