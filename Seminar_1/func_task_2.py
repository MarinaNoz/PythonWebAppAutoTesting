import json
import random
import string
import requests
import yaml

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)


def registration():
    set_char = string.ascii_letters + string.digits
    rand_email = ''.join(random.sample(set_char, 8))
    print(rand_email)
    headers = {
        'Content-type': 'application/json'
    }
    data = {
        'name': d['username'],
        'email': f'{rand_email}@dog.dog',
        'password': d['password']
    }

    result = requests.post(url=d['url_reg'], data=json.dumps(data), headers=headers)
    print(result.json()['data']['Token'])


def auth():
    headers = {
        # 'Authorization': f'Bearer {d["token"]}'
        'Content-type': 'application/json'
    }
    data = {

        'email': '9EvpRAZu@dog.dog',
        'password': d['password']
    }

    result = requests.post(url=d['url_auth'], data=json.dumps(data), headers=headers)
    return result.status_code


if __name__ == '__main__':
    auth()
