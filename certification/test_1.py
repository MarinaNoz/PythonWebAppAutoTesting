import datetime
import time
from testpage import *

from confest import *

with open('config.yaml') as f:
    config = yaml.safe_load(f)

login = config['username']
password = config['password']


def test_step1(check_invalid_credentials, browser):
    logging.info('test_1 running')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    testpage.get_err_text()
    assert testpage.get_err_text() == check_invalid_credentials


def test_step2(browser, check_hello_user):
    logging.info('test_2 running')
    testpage = OperationsHelper(browser)
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == check_hello_user


def test_step3(browser, check_find_about):
    logging.info('test_3 running')
    testpage = OperationsHelper(browser)
    testpage.click_about()
    time.sleep(1)
    assert testpage.about_size() == check_find_about

