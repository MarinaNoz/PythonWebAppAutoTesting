import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']

login = testdata['username']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
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
def expected_result_1():
    return '401'


@pytest.fixture()
def expected_result_2():
    return 'Hello, {}'.format(login)


@pytest.fixture()
def open_form():
    return 'Contact us!'


@pytest.fixture()
def alert_text():
    return 'Form successfully submitted'
