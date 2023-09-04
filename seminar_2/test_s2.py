from module import *
from time import *

with open('config.yaml') as f:
    config = yaml.safe_load(f)
site = Site(config['address'])
login = config['username']
password = config['password']


def test_step1(sel_1, x_selector2, btn_selector, x_selector3, result):
    site.find_element('xpath', sel_1).clear()
    site.find_element('xpath', sel_1).send_keys('err')

    site.find_element('xpath', x_selector2).clear()
    site.find_element('xpath', x_selector2).send_keys('err')

    site.find_element('css', btn_selector).click()

    err_label = site.find_element('xpath', x_selector3)
    res = err_label.text
    assert res == result


def test_step2(sel_1, x_selector2, btn_selector, auth, result2):

    site.find_element('xpath', sel_1).clear()
    site.find_element('xpath', sel_1).send_keys(login)
    site.find_element('xpath', x_selector2).clear()
    site.find_element('xpath', x_selector2).send_keys(password)
    btn = site.find_element('css', btn_selector)
    btn.click()

    auth = site.find_element('xpath', auth)
    res = auth.text
    assert res == result2


def test_step3(create_btn_selector, title, description, content, create, get_title):
    site.find_element('css', create_btn_selector).click()
    sleep(2)
    input_title = site.find_element('xpath', title)
    input_title.send_keys('Как управлять миром не привлекая внимания санитаров')
    input_description = site.find_element('xpath', description)
    input_description.send_keys('Шаг второй')
    input_content = site.find_element('xpath', content)
    input_content.send_keys('Попытка захватить мир тестирования используя Python и Selenium WebDriver')
    btn = site.find_element('xpath', create)
    sleep(2)
    btn.click()
    sleep(3)
    title = site.find_element('xpath', get_title)
    res = title.text
    site.close()
    assert res == 'Как управлять миром не привлекая внимания санитаров'