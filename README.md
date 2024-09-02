# useful_chunks

Scripts, chunks of code to perform various calculations and data manipulation

List of functions:
* dict_from_csv.py - create dictionary from csv-file located on disk. Keys = last column in csv-file, Values = first + ' ' + second columns in csv-file. Final dictionary is sorted by keys.
* dict_from_csv_url.py - create dictionary from csv-file located at url. Keys = last column in csv-file, Values = first + ' ' + second columns in csv-file. Final dictionary is sorted by keys.
Functions created while studying `Google IT Automation with Python`:
* start_date_report.py - script to get start_date from user, iterate over provided csv-file to build dictionary of dates-employees, compare provided start_date from user and dictionary of dates-employees and print list of dates-employees from start_date to the end of the dictionary. This script is from LAB: Debug and solve software problems, Program 4 'Troubleshooting and Debugging Techniques', Module 4 of Google IT Automation with Python.
* changeImage.py - script to open certain image files (with .tiff extension), resize them and save in .jpeg format
