#!/usr/bin/env python

#
# A Python script to collect the rankings for "Top Blockchain Dapps"
# The script is to provide the specified data, include step-by-step instructions,
# provide and CSV file for the basic information and a folder that contains
# all downloaded files.
# The data collected should include Rank, Name of Dapp, Name of Blockchain, Category
# Balance, No. of Users, Volume
# Downloading of the CSV file with longest time horizon is required, the CSV file
# should include the name of the Dapp and the collection data.
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
 

# PARAMETERS
URL = 'https://dappradar.com/rankings'

# SETTINGS FOR CHROME
chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(URL)
#title = driver.find_element(By.XPATH, '//div[1]/div[2]/div[1]/div[2]/section/div[1]/div[1]')
#elements = title.find_elements(By.TAG_NAME, 'a')
#data = []
#for e in elements:
#    data.append(e.text)
#print(data)

rankings_table = driver.find_element(By.XPATH, '//div[@class="sc-bQFuvY eZdjww rankings-table"]')
data = rankings_table.find_elements(By.TAG_NAME, 'a')
radar = []
for d in data:
    radar.append(d.text)
print(radar[1])
driver.quit()
