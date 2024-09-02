#! /usr/bin/env python3

import os
import requests

# Define file path to grab .txt files
path_to_files = '/data/feedback/'
# Define url to upload
url = 'http://IP_address/feedback/'
# Instantiate dictionary to be converted to json
content_dictionary = dict.fromkeys(['title', 'name', 'date', 'feedback'])
# Iterate over .txt files to populate dictionary
for filename in os.listdir(path_to_files):
    full_path_to_file = os.path.join(path_to_files, filename)
    # Check the path to the file and filter only files with .txt extension
    if os.path.isfile(full_path_to_file) and filename.endswith('.txt'):
        with open(full_path_to_file, mode = 'r') as file:
            lines = [line.rstrip('\n') for line in file] # Add list variable with all lines from .txt file
            content_dictionary['title'] = lines[0] # Populate dictionary according to keys
            content_dictionary['name'] = lines[1]
            content_dictionary['date'] = lines[2]
            content_dictionary['feedback'] = lines[3]
        # Print attempt to upload file
        print('Trying to upload content from:', filename)
        # Use post-request to the server
        response = requests.post(url, json = content_dictionary)
        # Raise error if server response not `201` = successful response
        if not response.ok:
            raise Exception('POST failed! | Status code: {} | File: {}'.format(response.status_code, filename))
        print('Feedback added! | Status code: {} | File: {}'.format(response.status_code, filename))
        file.close()