# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# https://sites.google.com/chromium.org/driver
service = Service(executable_path='chromedriver-linux64/chromedriver')

# Chrome brauzerini ishga tushirish
driver = webdriver.Chrome(service=service)

# Veb-sahifaga o'tish
driver.get('https://google.com')

# Sahifa sarlavhasini chop etish
print(f'Sahifa sarlavhasi: {driver.title}')

# 5 soniya kutish
time.sleep(5)

# Brauzerni yopish
driver.quit()