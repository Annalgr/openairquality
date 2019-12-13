"""
Get the value of an air quality parameter within a European city.
"""

import requests
import json
import csv


openaq_url = 'https://api.openaq.org/v1/latest?city={}&parameter={}'


def list_csv(csv_file):
    """Transform csv files into lists of elements."""
    e_list = []

    try:
        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                e_list = row
        return e_list

    except FileNotFoundError:
        return print("Input file does not exist.")

    except UnicodeDecodeError:
        return print("Invalid file type. CSV file required.")


def check_city(c):
    """Check that c is in the cities.csv"""
    c_list = list_csv('pypackage/cities.csv')
    if c.capitalize() in c_list:
        return True
    else:
        print("Oops! The European city you are looking for is not present.")
        return False


def get_quality(city, parameter):
    """Query the OpenAQ website to fetch the parameter's value.

       Key arguments:
       city -- European city name
       parameter -- name of the molecule
    """
    url = openaq_url.format(city.capitalize(), parameter)
    r = requests.get(url)
    data = json.loads(r.text)['results']
    p_value = 0

    if data:
        for d in data:
            measure = d['measurements'][0]
            p_value += measure['value']
        return p_value/len(data)
    return -1
