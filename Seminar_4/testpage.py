from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage, TestLocators):
    with open('config.yaml') as f:
        info = yaml.safe_load(f)

    def enter_bad_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['LOCATOR_LOGIN_FIELD'])
        if input1:
            input1.send_keys(self.info['err_login'])
        else:
            logging.error('The login field was not found')

    def enter_bad_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['LOCATOR_PASS_FIELD'])
        if input2:
            input2.send_keys(self.info['err_login'])
        else:
            logging.error('The password field was not found')

    def enter_good_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['LOCATOR_LOGIN_FIELD'])
        if input1:
            input1.send_keys(self.info['username'])
        else:
            logging.error('The login field was not found')

    def enter_good_pass(self):
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['LOCATOR_PASS_FIELD'])
        if input2:
            input2.send_keys(self.info['password'])
        else:
            logging.error('The password field was not found')

    def click_login_button(self):
        logging.debug('Click login button ')
        btn = self.find_element(self.ids['btn_selector'])
        if btn:
            btn.click()
        else:
            logging.error('Button not found')

    def get_error_text(self):
        err_label = self.find_element(self.ids['LOCATOR_ERR_FIELD'])
        if err_label:
            text = err_label.text
            logging.debug(f'Error {text} while loging')
            return text
        else:
            logging.error('The element with the error was not found')
            return None

    def get_hello_user(self):
        hello = self.find_element(self.ids['LOCATOR_AUTH'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('The user has not logged in')
            return None

    def click_contact_button(self):
        logging.debug('Click contact button ')
        cont_btn = self.find_element(self.ids['contact_btn'])
        if cont_btn:
            cont_btn.click()
        else:
            logging.error('The contact button was not found')

    def enter_name(self):
        logging.debug('Enter name ')
        name_input = self.find_element(self.ids['LOCATOR_NAME_INPUT'])
        if name_input:
            name_input.send_keys(self.info['username'])
        else:
            logging.error('The field for entering the name was not found')

    def enter_email(self):
        logging.debug('Enter email ')
        email_input = self.find_element(self.ids['LOCATOR_EMAIL'])
        if email_input:
            email_input.send_keys(self.info['email'])
        else:
            logging.error('The field for entering the email was not found')

    def enter_content(self):
        logging.debug('Enter content ')
        content_input = self.find_element(self.ids['LOCATOR_CONTENT_INPUT'])
        if content_input:
            content_input.send_keys(self.info['content'])
        else:
            logging.error('The content input field was not found')

    def click_contact_us_button(self):
        logging.debug('Click contact us button ')
        cont_us_btn = self.find_element(self.ids['LOCATOR_CONTACTUS_BTN'])
        if cont_us_btn:
            cont_us_btn.click()
        else:
            logging.error('The contact us button was not found')

    def switch_alert(self):
        logging.info('Switch alert')
        text = self.alert()
        logging.info(text)

    def click_alert_ok(self):
        logging.debug('Click alert ok ')
        alert_ok = self.driver.switch_to.alert()
        if alert_ok:
            alert_ok.accept()
        else:
            logging.error('The alert ok button was not found')
