#! /usr/bin/env python3

import os
import sys
import requests
import re

# Capture files that has the same filenames when excluding extensions
def same_file_name(folders):
    '''
    Compare file names excluding extensions in specified folders to define same-name-files
    '''
    # Instantiate list of sets to further unpack it ant implement intersection method
    sets_list = []

    # Iterate over the list of folders
    for folder in folders:
        # Create a set of file names (excluding extensions) for the iterable folder
        # link to formula|method: https://stackoverflow.com/a/73888266/22909975
        file_set = set(os.path.splitext(file)[0] for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file)))
        # Add this set to the `sets_list`
        sets_list.append(file_set)
    
    # Use set intersection to find common file names across all sets / folders
    if sets_list:
        common_files = set.intersection(*sets_list)  # *sets_list unpacks the list into arguments for intersection
    else:
        common_files = set()  # If no common files found between folders the resulting set will be empty
    return common_files


# Generate dictionary of file: extention pairs from two directories
def file_dictionary(folders):
    '''
    Generate dictionary of file name - file extension pairs.
    Usefull when dealing with identical file names with different extensions.
    '''
    # Instantiate dictionary to populate file_name - file_extention pairs
    dictionary = {}
    # Define needed extentions that will be kept in the dictionary
    needed_extentions = ['.txt', '.jpeg']
    # Iterate over given number of folders
    for index, item in enumerate(folders):
        # Iterate over files in folder
        for file in os.listdir(folders[index]):
            # Define full file path
            full_path_to_file = os.path.join(folders[index], file)
            # Check if the object in the folder ISFILE
            if os.path.isfile(full_path_to_file):
                # Instantiate dictionary key = file_name
                file_name = os.path.splitext(file)[0]
                # Instantiate dictionary value = file_extention
                file_extention = os.path.splitext(file)[1]
                # Iterate over found file names to append values to the dictionary
                if file_name not in dictionary:
                    dictionary[file_name] = []
                dictionary[file_name].append(file_extention)
    # Keep values = `file_extention` that is in `needed_extentions` list
    filtered_dictionary = {file_name: [extention for extention in file_extention if extention in needed_extentions] for file_name, file_extention in dictionary.items()}
    return filtered_dictionary


# Iterate through files in folders to populate json-dictionary and perform post-request
def dictionary_to_upload(file_list, file_folders, file_dictionary, url):
    '''
    Check given common files to:
    * parse text lines from .txt files
    * define identical file to .txt file (files have common names) - use its filename to use in post-request
    * perform post-request url, checking server response

    Function has limited capability - dealing only with two versions of identical file names:
    file_name1.txt - first file must be a .txt, to parse lines
    file_name1.jpeg - second file can be any
    '''
    # Instantiate dictionary to upload using json conversion
    content_to_upload = dict.fromkeys(['name', 'weight', 'description', 'image_name'])
    # Iterate over common files that was defined using `same_file_name` function
    for file in file_list:
        # Open file with identical name from 1 folder
        # KEEP IN MIND `replace` should be altered depending on hte operating system. current code is for windows machine
        with open(os.path.join(file_folders[0], (file + file_dictionary[file][0])), mode ='r') as source_1:
            # Open file with identical name from 2 folder
            with open(os.path.join(file_folders[1], (file + file_dictionary[file][1])), mode ='r') as source_2:
                # Parse text file from 1 folder by lines
                lines = [line.rstrip('\n') for line in source_1]
                # Assign each line to dictionary key - defined at the top
                content_to_upload['name'] = lines[0]
                content_to_upload['weight'] = int((re.search(r'\d+', lines[1])).group()) # The weight field is defined as an integer field.
                content_to_upload['description'] = lines[2]
                content_to_upload['image_name'] = file + file_dictionary[file][1]

            # Print each file content that is about to be uploaded using post-request
            print('Uploading following content: ', content_to_upload)
            # Use post-request to the server
            response = requests.post(url, json = content_to_upload)
            # Raise error if server response not `201` = successful response
            if not response.ok:
                raise Exception('POST failed! | Status code: {} | File: {}'.format(response.status_code, file))
            print('Feedback added! | Status code: {} | File: {}'.format(response.status_code, file))
            source_2.close()
        source_1.close()
    return


def main(argv):
    '''
    Script to:
    1. determine text and image files with the same names in given folders (number of folders is not limited)
    2. create dictionary of all file names and their extensions in given folders (number of folders is not limited)
    3. create json data from text (description) files and post it to web service using text data and corresponding image file name.
    
    !Keep in mind, that step (3) has limited capability - dealing only with two versions of identical file names.
    !If identical file names (but different extentions) would be more than 2 - update code!
    '''
    file_folders = ['/home/student/supplier-data/descriptions/',
                    '/home/student/supplier-data/images/']
    same_files_set = same_file_name(file_folders)
    f_dictionary = file_dictionary(file_folders)
    url = 'http://IP_address/fruits/'
    upload_data = dictionary_to_upload(same_files_set, file_folders, f_dictionary, url)
        

if __name__ == '__main__':
    main(sys.argv)