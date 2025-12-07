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
options.headless = False
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

# username = driver.find_element(By.NAME, 'username')
# username.send_keys('dvrkdev')  # input text

# email = driver.find_element(By.NAME, 'email')
# email.send_keys('diyorbek.qodirboyev05@gmail.com')

# password = driver.find_element(By.NAME, 'password')
# password.send_keys(os.environ.get('MY_PASSWORD'))

# bio = driver.find_element(By.NAME, 'bio')
# bio.send_keys('Python Developer')

# # Select elements
# country_element = driver.find_element(By.NAME, 'country')
# country = Select(country_element)
# # country.select_by_index(1)
# # country.select_by_value('ca')
# country.select_by_visible_text('Japan')

# for option in country.options:
# 	print(f'{option.text}: {option.get_attribute("value")}')

# # Multi-select elements
# languages_element = driver.find_element(By.NAME, 'languages')
# languages = Select(languages_element)
# languages.select_by_index(0)
# languages.select_by_value('es')
# languages.select_by_visible_text('French')

# selected_options = languages.all_selected_options
# for opt in selected_options:
# 	print(opt.text)

# time.sleep(3)

# languages.deselect_all()

# languages.select_by_index(1)

# Checkboxes and radio buttons
# interests = driver.find_elements(By.NAME, 'interests')

# interest = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//input[@name='interests' and @value='music']"))
# )

# driver.execute_script("arguments[0].scrollIntoView(true);", interest)
# time.sleep(0.2)
# driver.execute_script("arguments[0].click();", interest)


# # Check all the boxes
# for interest in interests:
# 	if not interest.is_selected():
# 		interest.click()

# time.sleep(2)

# # Uncheck all boxes
# for interest in interests:
# 	if interest.is_selected():
# 		interest.click()

# radios = driver.find_elements(By.NAME, 'gender')
# for r in radios:
# 	if r.get_attribute('value') == 'male':
# 		r.click()

# # Button
# btn = driver.find_element(By.ID, 'submit-btn')
# btn.click()


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



# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
