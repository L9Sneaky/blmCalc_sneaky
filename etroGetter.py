from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError


def get_set_from_etro(url):
    if(url == ""):
        return ""

    return_list = []
    gearset = urlparse(url).path.split('/')[2]
    new_url = 'https://etro.gg/api/gearsets/'+gearset+'/'

    try:
        response = requests.get(new_url)
        response.raise_for_status()
        response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return response
    return_list.append(response['totalParams'][17]['value'])
    return_list.append(response['totalParams'][0]['value'])
    return_list.append(response['totalParams'][3]['value'])
    return_list.append(response['totalParams'][4]['value'])
    return_list.append(response['totalParams'][5]['value'])
    return_list.append(response['totalParams'][6]['value'])
    return return_list

list = ['weapon', 'head', 'body', 'hands', 'legs', 'feet',
        'ears', 'neck', 'wrists', 'fingerL', 'fingerR', 'food']

url1 = 'https://etro.gg/gearset/2a195d7c-9078-4019-8c6f-1289b6ff9a13'
url2 = 'https://etro.gg/gearset/28423d0d-2583-494a-8fde-d0e41e4d1f12'

t1 = get_set_from_etro(url1)
t2 = get_set_from_etro(url2)
t1['materia']['36952']

for gear in list:
    print(gear + ' ' + str(t1[gear]))
    #
