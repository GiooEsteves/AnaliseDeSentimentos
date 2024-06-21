from textblob import TextBlob

def analyzeSentiment(text):
    blob = TextBlob(text)
    sentimentScore = blob.sentiment.polarity
    return sentimentScore
