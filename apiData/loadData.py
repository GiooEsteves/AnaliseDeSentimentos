import pandas as pd
import json
from textProcessing.preProcess import clean_tweets
from textProcessing.tokenizer import tokenizeText
from textProcessing.sentimentAnalysis import analyzeSentiment

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # Extraindo tweets da estrutura complexa do JSON
    tweets = []
    entries = data.get('data', {}).get('search_by_raw_query', {}).get('search_timeline', {}).get('timeline', {}).get('instructions', [])
    
    for entry in entries:
        if entry.get('type') == 'TimelineAddEntries':
            for item in entry.get('entries', []):
                tweet_data = item.get('content', {}).get('itemContent', {}).get('tweet_results', {}).get('result', {})
                tweet_core = tweet_data.get('core', {}).get('user_results', {}).get('result', {}).get('legacy', {})
                
                tweet_info = {
                    'tweet_id': tweet_data.get('rest_id'),
                    'created_at': tweet_core.get('created_at'),
                    'description': tweet_core.get('description'),
                    'followers_count': tweet_core.get('followers_count'),
                    'friends_count': tweet_core.get('friends_count'),
                    'name': tweet_core.get('name'),
                    'screen_name': tweet_core.get('screen_name'),
                    'statuses_count': tweet_core.get('statuses_count'),
                    'retweet_count': tweet_data.get('legacy', {}).get('retweet_count', 0),  # Número de RTs
                    'tweet_text': tweet_data.get('legacy', {}).get('full_text', '')  # Texto do tweet
                }
                
                tweets.append(tweet_info)
    
    df = pd.DataFrame(tweets)
    
    if 'tweet_text' in df.columns:
        df['cleaned_tweet'] = clean_tweets(df['tweet_text'])
        df['tokens'] = df['cleaned_tweet'].apply(tokenizeText)
        df['sentiment_score'] = df['cleaned_tweet'].apply(analyzeSentiment)
    
    return df
