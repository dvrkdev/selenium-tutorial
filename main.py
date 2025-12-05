# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# https://sites.google.com/chromium.org/driver
service = Service(executable_path='chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')

input_element = driver.find_element(By.NAME, 'q')
input_element.send_keys('Diyorbek Qodirboyev' + Keys.ENTER)


time.sleep(100)

driver.quit()