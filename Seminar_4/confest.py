import requests
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open('config.yaml') as f:
    config = yaml.safe_load(f)

browser = config['browser']
site = config['address']
login = config['username']
password = config['password']


@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def check_invalid_credentials():
    return "401"


@pytest.fixture()
def check_hello_user():
    return 'Hello, Petrucha1'


@pytest.fixture()
def check_alert_text():
    return 'Form successfully submitted'


@pytest.fixture()
def login_u():
    token_u = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': login, 'password': password})
    return token_u.json()['token']


@pytest.fixture()
def not_my_post():
    return 'Гепард,Лев,Антилопа'


@pytest.fixture()
def my_post():
    return 'Three children, Jeanne, Vincent'
