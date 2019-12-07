''' 
Get the value of an air quality parameter within a European city. 
'''


import requests
import json
import csv


openaq_url = 'https://api.openaq.org/v1/latest?city={}&parameter={}'


def list_csv(csv_file):
    '''Transform csv files into lists of elements.'''
    e_list = []
    with open(csv_file) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            e_list = row
    return e_list


def get_quality(city, parameter):
    '''Query the OpenAQ website to fetch the parameter's value.'''
    url = openaq_url.format(city, parameter)
    r = requests.get(url)
    data = json.loads(r.text)['results']
    p_value = 0
    
    if data:
        for d in data:
            measure = d['measurements'][0]
            p_value += measure['value']
        return p_value/len(data)
    return -1

