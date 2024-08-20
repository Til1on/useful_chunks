#!/usr/bin/env python3

import csv
import datetime
import requests


FILE_URL = 'https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv'

def get_start_date():
    '''Interactively get the start date to query for.'''

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def dict_from_csv_url(url_to_csv_file):
    '''
    Function can create dictionary based on csv-file from url
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

def get_same_or_newer(start_date, reader):
    '''Returns the employees that started on the given date, or the closest one.'''

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for key, values in reader.items():
        row_date = datetime.datetime.strptime(key, '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees += values

    return min_date, min_date_employees

def list_newer(start_date):
    reader = dict_from_csv_url(FILE_URL)
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date, reader)
        print(f'Started on {start_date.strftime('%b %d, %Y')}: {employees}')
        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == '__main__':
    main()
