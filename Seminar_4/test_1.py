import time
from testpage import *
from confest import *

with open('config.yaml') as f:
    config = yaml.safe_load(f)

login = config['username']
password = config['password']


def test_step1(check_invalid_credentials, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_bad_login()
    page.enter_bad_pass()
    page.click_login_button()
    assert page.get_error_text() == check_invalid_credentials


def test_step2(browser, check_hello_user, check_alert_text):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_pass()
    page.click_login_button()
    res1 = page.get_hello_user() == check_hello_user

    page.click_contact_button()
    time.sleep(3)
    page.enter_name()
    page.enter_email()
    page.enter_content()
    time.sleep(3)
    page.click_contact_us_button()
    time.sleep(1)
    page.click_alert_ok
    time.sleep(3)
    res2 = page.alert() == check_alert_text
    assert res1 and res2, 'test_step2 Fail'
