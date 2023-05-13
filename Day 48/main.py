from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re
import os

url = "http://orteil.dashnet.org/experiments/cookie/"
chrome_webdriver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_webdriver_path)
driver = webdriver.Chrome(service=service)


driver.get(url=url)
cookie_btn = driver.find_element(By.CSS_SELECTOR, "#middle > #cookie")
current_cookies = driver.find_element(By.CSS_SELECTOR, "#game > #money")
store_elements = driver.find_elements(By.CSS_SELECTOR, "#rightPanel > #store > div")
elements_by_id = [e.get_property("id") for e in store_elements]
store_prices = driver.find_elements(By.CSS_SELECTOR, "#rightPanel > #store > div > b")
timeout = time.time() + 5
end_time = time.time() + 300

while True:
    if time.time() >= end_time:
        end_cps = float(driver.find_element(By.ID, "cps").text.split(" ")[-1])
        break
    if time.time() > timeout:
        timeout = time.time() + 5
        store_prices = driver.find_elements(By.CSS_SELECTOR, "#rightPanel > #store > div > b")
        price_list = [int(re.sub(",", "", price.text.split(" ")[-1])) for price in store_prices
                      if re.sub(",", "", price.text.split(" ")[-1]) != ""]
        for price in price_list[::-1]:
            if int(current_cookies.text) >= price:
                idx = price_list.index(price)
                driver.find_element(By.ID, elements_by_id[idx]).click()
                break
    cookie_btn.click()

print(f"You ended with {end_cps} cookies per second after 5 minutes.")
