"""
Get the value of an air quality parameter within a European city:
verify that the user's input for the city is valid, if so query the
OpenAQ website to fetch the parameter's values and compute the avg.
"""

import requests
import json
import csv
import os


openaq_url = 'https://api.openaq.org/v1/latest?city={}&parameter={}'


def list_csv(csv_file):
    """Read csv file and store values into a list.

       Key arguments:
       csv_file -- csv file to be converted in py list
    """
    e_list = []

    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                e_list = row
        return e_list

    except FileNotFoundError:
        print("Input file does not exist.")
        return

    except UnicodeDecodeError:
        print("Invalid file encoding.")
        return


def check_city(c):
    """Check that the input city is in the European cities'list.

       Key arguments:
       c -- input city to look for
    """
    base_path = "pypackage"
    cities_file = "cities.csv"
    c_list = list_csv(os.path.join(base_path, cities_file))
    if c.capitalize() in c_list:
        return True
    else:
        print("Oops! The European city you are looking for is not present.")
        return False


def get_quality(city, parameter):
    """Query the OpenAQ website to fetch the parameter's value.
       The API returns json data, get all values from the same
       location and compute the average.

       Key arguments:
       city -- European city name
       parameter -- name of the polluting molecule
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
