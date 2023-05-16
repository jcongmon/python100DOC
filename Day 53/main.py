from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from data_parser import DataParser
import os

DRIVER_PATH = os.environ.get("DRIVER_PATH")
FORM_URL = os.environ.get("FORM_URL")


class DataInput:
    def __init__(self):
        self.service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.matrix = DataParser().data_matrix

    def submit_values(self):
        for i in range(len(self.matrix[0])):
            self.driver.get(url=FORM_URL)
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div"
                                               "/div[1]/div/div[1]/input").send_keys(self.matrix[0][i])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div"
                                               "/div[1]/div/div[1]/input").send_keys(self.matrix[1][i])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div"
                                               "/div[1]/div/div[1]/input").send_keys(self.matrix[2][i])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div").click()


data_entry = DataInput()
data_entry.submit_values()
