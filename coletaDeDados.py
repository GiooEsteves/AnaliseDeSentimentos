import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def obter_tweets_de_hoje(nome_perfil):
    url_base = f"https://twitter.com/{nome_perfil}"
    
    servico = Service(ChromeDriverManager().install())
    opcoes = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=servico, options=opcoes)
    
    driver.get(url_base)
    
    try:
        # Esperar até que os tweets estejam carregados
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweet"]'))
        )
        
        tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]')
        
        hoje = datetime.now().strftime('%d de %b')
        
        for tweet in tweets:
            try:
                # Esperar até que o texto do tweet esteja presente
                elemento_texto_tweet = WebDriverWait(tweet, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/div[2]/div[2]/div[1]'))
                )
                texto_tweet = elemento_texto_tweet.text
                
                # Encontra a data do tweet
                elemento_data_tweet = tweet.find_element(By.XPATH, './/time')
                data_tweet = elemento_data_tweet.get_attribute('datetime')
                data_tweet_formatada = datetime.strptime(data_tweet, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d de %b')
                
                if data_tweet_formatada == hoje:
                    print(texto_tweet)
            except Exception as e:
                print(f"Erro ao extrair o texto ou data do tweet: {e}")
    except Exception as e:
        print(f"Erro ao carregar a página ou encontrar tweets: {e}")
    finally:
        driver.quit()

obter_tweets_de_hoje('raquellyra')
