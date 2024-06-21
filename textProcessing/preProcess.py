import re
import emoji
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    tweet = emoji.demojize(tweet)
    tweet = re.sub(r':[a-zA-Z_]+:', '', tweet)
    tweet = re.sub(r'\d+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet = tweet.strip()
    tweet = ' '.join([word for word in tweet.split() if word.lower() not in stop_words])
    
    return tweet

def clean_tweets(tweets):
    return [clean_tweet(tweet) for tweet in tweets]
