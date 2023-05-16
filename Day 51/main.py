from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from json_handler import JSONHandler

AMEX_URL = os.environ.get("AMEX_URL")
DRIVER_PATH = os.environ.get("DRIVER_PATH")
TWITTER_URL = os.environ.get("TWITTER_URL")
TWITTER_USER = os.environ.get("TWITTER_USER")
TWITTER_PASSWORD = os.environ.get("TWITER_PASSWORD")

data = JSONHandler()

if data.update_twitter:
    service = Service(executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(url=TWITTER_URL)
    time.sleep(5)
    sign_in_email = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe")
    sign_in_email.send_keys(TWITTER_USER)
    sign_in_email.send_keys(Keys.ENTER)

    time.sleep(20)

    ###### LOGIN WITHOUT CAPTCHA #######

    # password_input = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1niwhzg")
    # password_input.send_keys(os.environ.get("TWITTER_PASSWORD"))
    # driver.find_element(By.CSS_SELECTOR, "div.css-901oao.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q"
    #                                      ".r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0").click()
    # time.sleep(5)

    enter_tweet = driver.find_element(By.CSS_SELECTOR,
                                      "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
    enter_tweet.click()
    enter_tweet.click()
    enter_tweet.click()     # Bypass popups
    for idx, entry in data.new_deals.items():
        enter_tweet.click()
        entry_str = f"New deal: {entry['name']} with a {entry['percentage']} bonus ({entry['conversion']}). " \
                    f"Ends on {entry['end_date']}."
        enter_tweet.send_keys(entry_str)
        enter_tweet.send_keys(Keys.COMMAND, Keys.ENTER)
        time.sleep(2)
        enter_tweet = driver.find_element(By.CSS_SELECTOR,
                                          "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        enter_tweet.click()
        time.sleep(1)
    time.sleep(10)
    driver.quit()
