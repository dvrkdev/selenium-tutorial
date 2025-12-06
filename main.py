# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver
service = Service(executable_path='chromedriver-linux64/chromedriver')

options = Options()
options.headless = True
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.page_load_strategy = 'eager'

# Chrome brauzerini ishga tushirish
driver = webdriver.Chrome(options=options, service=service)
# driver = webdriver.Chrome(options=options)

# Veb-sahifaga o'tish
driver.get('https://techbeamers.com/selenium-practice-test-page/')
# driver.get('https://instagram.com')

# Sahifa sarlavhasini chop etish
print(f'Sahifa sarlavhasi: {driver.title}')

# # ID bo'yicha element topish
# element_by_id = driver.find_element(By.ID, 'username')
# element_by_id.send_keys('dvrkdev')

# # Name bo'yicha element topish
# element_by_name = driver.find_element(By.NAME, 'username')
# element_by_name.send_keys('dvrkdev')

# Class nomi bo'yicha element topish
# element_by_class = driver.find_element(By.CLASS_NAME, 's-title')
# print(element_by_class.text)

# # XPath bo'yicha element topish
# element_by_xpath = driver.find_element(By.XPATH, '//input[@type="email"]')
# print(element_by_xpath)

# # CSS selector bo'yicha element topish
# element_by_css = driver.find_element(By.CSS_SELECTOR, 'a.meta-author')
# print(element_by_css.text)

# username = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.ID, 'username')))
# username.send_keys('dvrkdev')

# Jadvalni kutib olish
table = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.ID, "pagination-table")))
# Barcha qatorlarni olish
rows = table.find_elements(By.TAG_NAME, 'tr')  # find_elements -> plural
# print(rows)
print(f'Jami qatorlar: {len(rows)}')

# Qator ichidagi ustunga tegishli matnlarni chiqarish
for i, row in enumerate(rows):
	cells = row.find_elements(By.TAG_NAME, 'td')
	cell_texts = [cell.text for cell in cells]
	print(f'{i}-qator: {cell_texts}')

# 5 soniya kutish
time.sleep(5)

# Brauzerni yopish
driver.quit()