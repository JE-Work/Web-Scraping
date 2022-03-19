#!/usr/bin/env python3

# A SCRIPT TO FETCH AND SAVE IMAGES FROM AN API

import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time

# PARAMETERS
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}
URL = 'https://example.com/api/v1/Image/GetImage/'
FILTER = [1545]

# FETCH IMAGES
def fetch_image(url, num):

    # CREATE THE URL FOR EACH IMAGE
    image_url = f'{url}{num}'

    # CREATE FILENAME FROM URL
    filename = image_url.rsplit('/', 1)[-1]+'.jpeg'

    # PARAMETERS FOR RETRY STRATEGY
    retry_params = Retry(
        total=5,
        status_forcelist=[429, 500, 503],
        backoff_factor=10
    )
    adapter = HTTPAdapter(max_retries=retry_params)
    http = requests.Session()
    http.mount("https://", adapter)
    
    # FETCH IMAGE WITH FILTERING FOR NO-IMAGE
    img = http.get(f'{image_url}', headers=HEADERS)
    if len(img.content) in FILTER:
        print('non-image')
        pass
    else:
        # WRITE IMAGE TO FILE
        print(f'{filename}')
        print('image saved')
        with open (filename, 'wb') as file:
            file.write(img.content)

    # IMPLEMENT A SLEEP TIMER TO AVOID RATE LIMIT
    time.sleep(img.elapsed.total_seconds())


def main():
  
    #TEST RANGE OF IMAGES
    for i in range (6216350, 6216850):
        fetch_image(URL, i)

if __name__ == '__main__':
    main()
