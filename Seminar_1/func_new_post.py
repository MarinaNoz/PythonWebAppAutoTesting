import json
import random
import string
import requests
import yaml

with open('config.yaml', 'r') as f:
    d = yaml.safe_load(f)


def auth_admin():
    data = {'username': d['admin'],
            'password': d['admpas']
            }
    res = requests.post(url=d['url_auth_gb'], data=data)
    print(res.json()['token'])
    return res.json()['token']


def auth_user():
    headers = {
        'Authorization': f'Bearer{d["X-Auth-Token"]}'
    }
    data = {
        'username': d["username"],
        'password': d["password"],
    }
    result = requests.post(url=d['url_auth_gb'], data=data, headers=headers)

    print(result.status_code)
    return result.status_code


def new_posts():
    headers = {
        'X-Auth-Token': d["X-Auth-Token"]
    }
    data = {
        'title': 'This is my first post from API',
        'description': 'First post from API',
        'content': 'Добавить в задание с REST API еще один текст,'
                   'в котором создается новый пост, а потом проверяется'
                   'его наличие на сервере по полю "описание"'
    }

    result = requests.post(url=d['url_posts_gb'], data=data, headers=headers)
    # print(result.status_code)
    return result.status_code, result.json()['description']


# def check_posts():
#     headers = {
#         'Authorization': f'Bearer{d["X-Auth-Token"]}'
#     }
#     data = {
#         'username': d["username"],
#         'password': d["password"],
#     }
#     result = requests.post(url=d['url_auth_gb'], data=data, headers=headers)
#     result_dict = result.json()
#     pretty = json.dumps(result_dict, indent=4)
#     # print(result.status_code)
#     print(pretty)
#     return result.status_code, result.json()


if __name__ == '__main__':
    # auth_admin()
    # auth_user()
    print(new_posts('First post from API'))
    # print(check_posts())
