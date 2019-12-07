"""
 Create csv files for limiting user's request of cities and parameters.
"""

import csv
import requests
import json


def has_numbers(input_s):
    '''Check if the string contains digits.'''
    return any(char.isdigit() for char in input_s)


def check_city(data):
    '''Data cleaning and filtering for European cities.'''
    eu = []
    with open('eu.csv') as eu_file:
        reader = csv.reader(eu_file, delimiter=',')
        for row in reader:
            eu = row

    city_list =[]
    for d in data:
        if d['country'] in eu:
            eu_city = d['city']
            if eu_city != 'N/A' and eu_city != 'unused' and not has_numbers(eu_city):
                city_list.append(eu_city)

    return city_list


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


if __name__ == "__main__":
    url_c = 'https://api.openaq.org/v1/cities?limit=10000'  
    url_p = 'https://api.openaq.org/v1/parameters'

    cities = create_csv(url_c, 'city', 'cities.csv')
    parameters = create_csv(url_p, 'id', 'parameters.csv')
