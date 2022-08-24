from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError


def get_set_from_etro(url):
    if(url == ""):
        return ""

    return_list = {}
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

    # return response
    return_list['WD'] = 126
    return_list['Int']=response['totalParams'][0]['value']
    return_list['DH']=response['totalParams'][3]['value']
    return_list['Crit']=response['totalParams'][4]['value']
    return_list['Det']=response['totalParams'][5]['value']
    return_list['Sps']=response['totalParams'][6]['value']
    return return_list



# path = 'https://etro.gg/gearset/54c74fd7-f9b6-4c1b-9440-87c4f2e6e62b'
# a = get_set_from_etro(path)
# a
