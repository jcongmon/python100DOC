from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

URL = os.environ.get("URL")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DRIVER_PATH = os.environ.get("DRIVER_PATH")

service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(url=URL)

signin_btn = driver.find_element(By.LINK_TEXT, "Sign in")
signin_btn.click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(USER)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

while True:
    try:
        all_jobs = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container > li")
        for job in all_jobs:
            job.click()
            time.sleep(2)
            try:
                driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card > button").click()
                submit_application_btn = driver.find_element(By.CSS_SELECTOR, "footer > div > button.artdeco-button > span")
                if submit_application_btn.text == "Submit application":
                    submit_application_btn.click()
                    time.sleep(3)
                    driver.find_element(By.CSS_SELECTOR, "div.artdeco-modal > button.artdeco-modal__dismiss").click()  # DISMISS
                else:
                    driver.find_element(By.CSS_SELECTOR, "div.artdeco-modal > button.artdeco-modal__dismiss").click()   # DISMISS
                    time.sleep(2)
                    driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar--confirm-dialog > button").click()  # DISCARD
                    time.sleep(2)
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        driver.quit()
    try:
        next_page = driver.find_elements(By.CSS_SELECTOR, "ul.artdeco-pagination__pages--number > li")[1]
    except NoSuchElementException:
        driver.quit()
    else:
        next_page.click()
        time.sleep(5)
