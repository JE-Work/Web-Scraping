#!/usr/bin/env python

#
# This project was a simple task to mimic a human interacting with a news site.
# As a POC this script will visit reuters news home page, and scroll down the
# article listings and back up.
# It will then visit one of three sections scrolling down the whole page then
# back up.
# Finally it will use the search bar to look up one of four search terms.
#

import numpy as np
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  

# HOMEPAGE
URL = 'https://www.reuters.com/'

# SETTINGS FOR FIREFOX
driver = webdriver.Firefox()

TABS = ['markets', 'technology', 'business']
SEARCH = ['Electric Cars','Tesla', 'Polestar', 'Rivian']

driver.get(URL)
footer = driver.find_element(By.XPATH, '//div[@class="landing-layout__footer__3JQMs"]')
time.sleep(2)

# SCROLL DOWN THEN UP THE HOMEPAGE
home_page = driver.find_element(By.XPATH, '//div[@class="home-page-grid__wrapper__1Th0u"]')
home_loc = home_page.location
home_size = home_page.size
y_start = home_loc['y']
height = home_size['height']
for i in np.arange(y_start, height, random.uniform(0.09, 0.3)):
    driver.execute_script(f'window.scrollTo(0, {i});')
    current = i
time.sleep(2)
for i in reversed(np.arange(y_start, height, random.uniform(0.1, 0.3))):
    driver.execute_script(f'window.scrollTo(0, {i});')
time.sleep(2)

# NAVIGATE TO NEW SECTION 
random_tab = random.choice(TABS)
driver.get(f'{URL}{random_tab}')
main_content = driver.find_element(By.XPATH, '//main[@id="main-content"]')
main_loc = main_content.location
main_size = main_content.size
start_y = main_loc['y']
main_height = main_size['height']
for i in np.arange(start_y, main_height, random.uniform(0.1, 0.3)):
    driver.execute_script(f'window.scrollTo(0, {i});')
    current = i
time.sleep(1)
for i in reversed(np.arange(start_y, main_height, random.uniform(0.1, 0.4))):
    driver.execute_script(f'window.scrollTo(0, {i});')
    current = i
time.sleep(1)

# USE SEARCH BAR
random_search = random.choice(SEARCH)
search_field = driver.find_element(By.XPATH, '//button[@aria-label="Open search bar"]').click()
search_bar = driver.find_element(By.XPATH, '//input[@type="search"]')
search_bar.send_keys(random_search, Keys.ENTER)
time.sleep(5)

driver.quit()
