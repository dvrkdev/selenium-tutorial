# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time

load_dotenv()

# https://sites.google.com/chromium.org/driver
service = Service(executable_path='chromedriver-linux64/chromedriver')

options = Options()
options.headless = True
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.page_load_strategy = 'eager'

# Launch Chrome
driver = webdriver.Chrome(options=options, service=service)
# driver = webdriver.Chrome(options=options)

# Navigate to the webpage
driver.get('https://techbeamers.com/selenium-practice-test-page/')
# driver.get('https://instagram.com')

# Print page title
print(f'Page title: {driver.title}')


# ==== SELECTING ELEMENTS ====

# # Find element by ID
# element_by_id = driver.find_element(By.ID, 'username')
# element_by_id.send_keys('dvrkdev')

# # Find element by Name
# element_by_name = driver.find_element(By.NAME, 'username')
# element_by_name.send_keys('dvrkdev')

# Find element by Class name
# element_by_class = driver.find_element(By.CLASS_NAME, 's-title')
# print(element_by_class.text)

# # Find element by XPath
# element_by_xpath = driver.find_element(By.XPATH, '//input[@type="email"]')
# print(element_by_xpath)

# # Find element by CSS selector
# element_by_css = driver.find_element(By.CSS_SELECTOR, 'a.meta-author')
# print(element_by_css.text)

# username = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.ID, 'username')))
# username.send_keys('dvrkdev')


# ==== PERFORMING ACTIONS ====

username = driver.find_element(By.NAME, 'username')
username.send_keys('dvrkdev')  # input text

email = driver.find_element(By.NAME, 'email')
email.send_keys('diyorbek.qodirboyev05@gmail.com')

password = driver.find_element(By.NAME, 'password')
password.send_keys(os.environ.get('MY_PASSWORD'))

bio = driver.find_element(By.NAME, 'bio')
bio.send_keys('Python Developer')

# Select elements
select_element = driver.find_element(By.NAME, 'country')
select = Select(select_element)
# select.select_by_index(1)
# select.select_by_value('ca')
select.select_by_visible_text('Japan')

for option in select.options:
	print(f'{option.text}: {option.get_attribute("value")}')

# Multi-select elements
multi_select_element = driver.find_element(By.NAME, 'languages')
multi_select = Select(multi_select_element)
multi_select.select_by_index(0)
multi_select.select_by_value('es')
multi_select.select_by_visible_text('French')

selected_options = multi_select.all_selected_options
for opt in selected_options:
	print(opt.text)

time.sleep(3)

multi_select.deselect_all()


# ==== WORKING WITH TABLES ====

# # Wait for the table
# table = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.ID, "pagination-table")))
# # Get all rows
# rows = table.find_elements(By.TAG_NAME, 'tr')  # find_elements -> plural
# # print(rows)
# print(f'Total rows: {len(rows)}')

# # Print cell text for each row
# for i, row in enumerate(rows):
# 	cells = row.find_elements(By.TAG_NAME, 'td')
# 	cell_texts = [cell.text for cell in cells]
# 	print(f'Row {i}: {cell_texts}')



# # Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
