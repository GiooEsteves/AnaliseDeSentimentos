import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scroll_pagina(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        
        last_height = new_height

def obter_tweets(nome_perfil):
    url_base = f"https://twitter.com/{nome_perfil}"
    
    servico = Service(ChromeDriverManager().install())
    opcoes = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=servico, options=opcoes)
    
    driver.get(url_base)
    
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweet"]'))
        )
        
        scroll_pagina(driver)
        
        tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]')
        
        for tweet in tweets:
            try:
                elemento_texto_tweet = WebDriverWait(tweet, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/div[2]/div[2]/div[1]'))
                )
                texto_tweet = elemento_texto_tweet.text
                
                elemento_data_tweet = tweet.find_element(By.XPATH, './/time')
                data_tweet = elemento_data_tweet.get_attribute('datetime')
                data_tweet_formatada = datetime.strptime(data_tweet, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d de %b')
                
                print(f"Data do tweet: {data_tweet_formatada}")
                print(f"Tweet: {texto_tweet}")
                print("-" * 50)
                
            except Exception as e:
                print(f"Erro ao extrair o texto ou data do tweet: {e}")
    
    except Exception as e:
        print(f"Erro ao carregar a página ou encontrar tweets: {e}")
    
    finally:
        driver.quit()

obter_tweets('raquellyra')
