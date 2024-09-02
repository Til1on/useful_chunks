# useful_chunks

Scripts, chunks of code to perform various calculations and data manipulation.

List of functions:
* dict_from_csv.py - create dictionary from csv-file located on disk. Keys = last column in csv-file, Values = first + ' ' + second columns in csv-file. Final dictionary is sorted by keys.
* dict_from_csv_url.py - create dictionary from csv-file located at url. Keys = last column in csv-file, Values = first + ' ' + second columns in csv-file. Final dictionary is sorted by keys.


Functions created while studying `Google IT Automation with Python`:
* start_date_report.py - script to get start_date from user, iterate over provided csv-file to build dictionary of dates-employees, compare provided start_date from user and dictionary of dates-employees and print list of dates-employees from start_date to the end of the dictionary. This script is from LAB: Debug and solve software problems, Course 4 - Troubleshooting and Debugging Techniques.
* course6_module2_run.py - script to upload json formatted data to the web-server using post-request. Script is reading .txt files from given directory line by line and populate dictionary using predefined keys and values that corresponds to certain lines of the .txt file. This script is from LAB: Processing Text Files with Python Dictionaries and Uploading to Running Web Service, Course 6 - Automating Real-World Tasks with Python.
* course6_module3_cars.py - script to create pdf document from json file and send it via email. Script process data using dictionaries, sorting, calculating maximums. PDF creation using table styles, paragraph styles, pie-chart building. This script is from LAB: Automatically Generate a PDF and sending it by E-mail, Course 6 - Automating Real-World Tasks with Python.
* changeImage.py - script to open certain image files (with .tiff extension), resize them and save in .jpeg format
* supplier_image_upload.py - script to upload images converted by 'changeImage.py' to provided IP-address.
