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
        response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    # return response
    for i in response['totalParams']:
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

# %%
# import coreapi
#
# # Initialize a client & load the schema document
# client = coreapi.Client()
# schema = client.get("https://etro.gg/api/docs/")
# def get_gear(url):
#     gearset = urlparse(url).path.split('/')[2]
#     # Interact with the API endpoint
#     action = ["gearsets", "read"]
#     params = {
#         "id": gearset,
#     }
#     return client.action(schema, action, params=params)
