import requests
import json


openaq_url = 'https://api.openaq.org/v1/latest?city={}&parameter={}'


def get_quality(city, parameter):
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

