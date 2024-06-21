from apiData.apiClient import fetch_data_from_api
from textProcessing.preProcess import clean_tweet
from textProcessing.tokenizer import tokenize_text
from textProcessing.sentimentAnalysis import analyze_sentiment

def main():
    api_url = "" 
    
    try:
        data = fetch_data_from_api(api_url)
    except Exception as e:
        print(f"Erro ao carregar dados da API: {e}")
        return
    
    cleaned_texts = []
    for item in data['items']:
        text = item['text']
        cleaned_text = clean_tweet(text)
        cleaned_texts.append(cleaned_text)
    
    tokenized_texts = []
    for text in cleaned_texts:
        tokens = tokenize_text(text)
        tokenized_texts.append(tokens)
    
    sentiment_scores = []
    for tokens in tokenized_texts:
        text = ' '.join(tokens) 
        sentiment_score = analyze_sentiment(text)
        sentiment_scores.append(sentiment_score)
    
if __name__ == "__main__":
    main()
