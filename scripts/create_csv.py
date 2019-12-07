"""
 Create csv files for limiting user's request of cities and parameters.
"""

import csv
import requests
import json


def has_numbers(input_s):
    '''Check if the string contains digits.'''
    return any(char.isdigit() for char in input_s)


def create_csv(url, req, csv_name):
    '''Gather data from OpenAir APIs and create a csv file.'''
    q = requests.get(url)
    data = json.loads(q.text)['results']

    res_list = []  # define the list of results

    if req == 'city':
        res_list = check_city(data)

    elif req == 'id':
        for d in data:
            res_list.append(d[req])

    results_file = open(csv_name, 'w') # open a new file

    for r in res_list: # write data into the file
        results_file.write(r + ",")
    results_file.close()

    return results_file
