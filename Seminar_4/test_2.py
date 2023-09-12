from testpage import *
from confest import *


with open('config.yaml') as f:
    config = yaml.safe_load(f)

password = config['password']
token = config['token']
content = config['content']


def get_my_posts(token_u):
    logging.debug('Open posts page')
    my_posts = requests.get('https://test-stand.gb.ru/api/posts',
                     headers={'X-Auth-Token': token_u})
    if my_posts:
        listcont = [i['content'] for i in my_posts.json()['data']]
        return listcont
    else:
        logging.error('Страница с постами не открылась')


def get_not_my_posts(token_u):
    logging.debug('Open posts page')
    not_my_posts = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token_u},
                     params={'owner': 'notMe'})
    if not_my_posts:
        listcont = [i['content'] for i in not_my_posts.json()['data']]
        return listcont
    else:
        logging.error('Страница с постами не открылась')


def test_create_post(login_u):
    logging.debug('Create new post')
    create_post = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
                      data={'title': 'Создание поста через API v2',
                            'description': 'informaition about post',
                            'content': f'{content}'})
    if create_post:
        return create_post.json()
    else:
        logging.error('Пост не создан')


def test_find_post(login_u):
    logging.debug('Find created post')
    find_post = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    if find_post:
        listdescript = [i['description'] for i in find_post.json()['data']]
        return listdescript
    else:
        logging.error('Пост не найден')


def test_not_my_post(login_u, not_my_post):
    assert not_my_post in get_not_my_posts(login_u)


def test_my_post(login_u, my_post):
    assert any(my_post in s for s in get_my_posts(login_u))
