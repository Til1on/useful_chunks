#!/usr/bin/env python3

import csv
import requests

def dict_from_csv_url(url_to_csv_file):
    '''
    Fucntion can create dictionary based on csv-file from url
    Keys-values pairs can be adjusted
    Keys = last column in csv-file
    Values = first + ' ' + second columns in csv-file
    Final dictionary is sorted by keys
    '''

    # Instantiate empty dictionary
    dictionary = {}
    # Open csv-file in read-only mode using UTF-8 encoding
    with requests.Session() as req_session:
        download = req_session.get(url_to_csv_file, stream=False)
        decoded = download.content.decode('UTF-8')
        # Use csv.reader method, specify delimiter
        reader = csv.reader(decoded.splitlines(), delimiter = ',')
        # Skip first row containing column headers
        next(reader)
        for row in reader:
            # Using last column as key
            key = row[-1]
            # Using first and second columns as values
            value_0 = row[0]
            value_1 = row[1]
            # Populate dictionary
            if key not in dictionary:
                dictionary[key] = []
            # Concatinate values from first and second columns into one with empty space between
            value_con = value_0 + ' ' + value_1
            dictionary[key].append(value_con)
    req_session.close()
    # Sort populated dictionary by keys
    dictionary_sorted = dict(sorted(dictionary.items()))
    return dictionary_sorted
