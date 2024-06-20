import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files\drivers\chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")

# Wait for the username input field to load
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "session[username_or_email]")))
username_input.send_keys("")

# Click the Next button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
next_button.click()

# Wait for the password input field to load
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "session[password]")))
password_input.send_keys('')

# Click the Log in button
log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']")))
log_in_button.click()

# Wait for the search box to load
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")))
search_box.send_keys("Raquel Lyra")
search_box.send_keys(Keys.ENTER)

# Wait for the People tab to load and click it
people_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='People']")))
people_tab.click()

# Wait for profile link to load and click it (assuming it's the first result)
profile_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='UserCell']//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']/span")))
profile_link.click()

# Initialize lists to store data
UserTags = []
TimeStamps = []
Tweets = []
Replys = []
reTweets = []
Likes = []

# Function to collect tweet data
def collect_tweet_data(article):
    try:
        UserTag = article.find_element(By.XPATH, ".//div[@data-testid='UserNames']").text
        TimeStamp = article.find_element(By.XPATH, ".//time").get_attribute('datetime')
        Tweet = article.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        Reply = article.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        reTweet = article.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        Like = article.find_element(By.XPATH, ".//div[@data-testid='like']").text
        return UserTag, TimeStamp, Tweet, Reply, reTweet, Like
    except:
        return None, None, None, None, None, None

# Scroll and collect tweets until we have 5 unique ones
while len(set(Tweets)) < 5:
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    for article in articles:
        data = collect_tweet_data(article)
        if data:
            UserTags.append(data[0])
            TimeStamps.append(data[1])
            Tweets.append(data[2])
            Replys.append(data[3])
            reTweets.append(data[4])
            Likes.append(data[5])
            # Print each tweet data
            print(f"User: {data[0]}")
            print(f"Timestamp: {data[1]}")
            print(f"Tweet: {data[2]}")
            print(f"Reply: {data[3]}")
            print(f"Retweets: {data[4]}")
            print(f"Likes: {data[5]}")
            print("="*50)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    WebDriverWait(driver, 10).until(EC.staleness_of(articles[-1]))  # Wait for new tweets to load

# Close the browser
driver.quit()
