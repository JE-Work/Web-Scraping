#!/usr/bin/env python

# A Python script that takes a provided file of URLs from the CLI, and attempts
# to capture a screenshot of each URL using a headless Chrome browser,
# and stores them in a separate directory.

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ScreenshotException
from selenium.common.exceptions import TimeoutException
import time

# CREATE DIRECTORY TO STORE SCREENSHOTS
os.makedirs('screenshots',exist_ok=True)
PATH = os.getcwd() + '/screenshots/'

# SETTINGS FOR BROWSER
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(5)

def screenshot(url):
    filename = os.path.splitext(url)[0]+'.png' 
    try:
        driver.get(f'https://{url}')
        time.sleep(5)
        driver.get_screenshot_as_file(f'{PATH}/{filename}')
        print(f'[+]{url} captured!')
    except ScreenshotException:
        print('A screen capture was made impossible')
    except TimeoutException:
        print('Loading took to much time')

def main():
	
    with open(sys.argv[1]) as f:
        urls = [line.strip() for line in f.readlines()]
        for url in urls:
            screenshot(url)
    driver.quit()

if __name__ == '__main__':
	main()
