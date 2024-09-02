#!/usr/bin/env python3

import requests
import os

# Define url to upload
url = 'http://IP_address/upload/'
# Define file path to grab images to upload
path_to_files = '/home/student/supplier-data/images/'

# Iterate over files on given folder
for filename in os.listdir(path_to_files):
    # Filter only files with .jpeg extension
    if filename.endswith('.jpeg'):
        with open(path_to_files + filename, 'rb') as opened:
            # Use post-request to the server
            response = requests.post(url, files={'file': opened})
            # Raise error if server response not `201` = successful response
            if not response.ok:
                raise Exception('POST failed! | Status code: {} | File: {}'.format(response.status_code, filename))
            print('File uploaded! | Status code: {} | File: {}'.format(response.status_code, filename))
            opened.close()
