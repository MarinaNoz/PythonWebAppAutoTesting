from time import *
from testpage import *
from confest import *

with open('config.yaml') as f:
    config = yaml.safe_load(f)

site = config['address']
login = config['username']
password = config['password']
err_login = config['err_login']
err_pass = config['err_pass']
content = config['content']

def test_step1(expected_result_1, browser):
    logging.info('Test1 Starting')
    site = Operations(browser)
    site.go_to_site()
    site.enter_login(err_login)
    site.enter_pass(err_pass)
    site.click_login_button()
    assert site.get_error_text() == expected_result_1


def test_step2(expected_result_2, browser):
    logging.info('Test2 Starting')
    testpage = Operations(browser)
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.check_enter_user() == expected_result_2


def test_step3(open_form, browser):
    logging.info('Test3 Starting')
    testpage = Operations(browser)
    testpage.button_contact()
    sleep(3)
    assert testpage.check_open_form() == open_form


def test_step4(alert_text, browser):
    logging.info('Test4 Starting')
    testpage = Operations(browser)
    testpage.button_contact()
    testpage.input_form_name(login)
    testpage.input_form_email(f'{login}@email.ru')
    testpage.input_form_content(f'{content}')
    testpage.contact_us_btn()
    sleep(3)
    assert testpage.check_alert_text() == alert_text
