from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError


def get_set_from_etro(url):
    if(url == ""):
        return ""
    return_list = {'WD': 0, 'Int': 0, 'DH': 0, 'Crit': 0, 'Det': 0, 'Sps': 0}
    gearset = urlparse(url).path.split('/')[2]
    new_url = 'https://etro.gg/api/gearsets/'+gearset+'/'

    try:
        response = requests.get(new_url)
        response.raise_for_status()
        json_response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        # return response
        for i in json_response['totalParams']:
            if i['name'] == 'Weapon Damage':
                return_list['WD']=i['value']

            if i['name'] == 'INT':
                return_list['Int']=i['value']

            if i['name'] == 'DH':
                return_list['DH']=i['value']

            if i['name'] == 'CRT':
                return_list['Crit']=i['value']

            if i['name'] == 'DET':
                return_list['Det']=i['value']

            if i['name'] == 'SPS':
                return_list['Sps']=i['value']
        return return_list



# %%
import coreapi

def get_set_from_etro2(url):
    if(url == ""):
        return ""
    return_list = {'WD': 0, 'Int': 0, 'DH': 0, 'Crit': 0, 'Det': 0, 'Sps': 0}
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("https://etro.gg/api/docs/")

    # Interact with the API endpoint
    action = ["gearsets", "read"]
    params = {
        "id": url.split('/')[-1],
    }
    try:
        result = client.action(schema, action, params=params)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        for i in result['totalParams']:
            if i['name'] == 'Weapon Damage':
                return_list['WD']=i['value']

            if i['name'] == 'INT':
                return_list['Int']=i['value']

            if i['name'] == 'DH':
                return_list['DH']=i['value']

            if i['name'] == 'CRT':
                return_list['Crit']=i['value']

            if i['name'] == 'DET':
                return_list['Det']=i['value']

            if i['name'] == 'SPS':
                return_list['Sps']=i['value']
        return return_list

# a = get_set_from_etro2('https://etro.gg/gearset/d6c0b7f7-21c4-451c-88f0-ddb867bd19d3')
# path = 'https://etro.gg/gearset/bdf03606-6cf5-41fb-ad39-fe5a58ca7e72'
# a = get_set_from_etro2(path)
# print(a)