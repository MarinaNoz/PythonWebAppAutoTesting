from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_BUTTON = (By.CSS_SELECTOR, "button")
    LOCATOR_ERR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_AUTH = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_TITLE_FORM = (By.XPATH, '//*[@id="app"]/main/div/div/h1')
    LOCATOR_NAME_INPUT = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_E_MAIL = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT_INPUT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACTUS_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class Operations(BasePage, TestLocators):

    def enter_login(self, word):
        logging.info(f'Enter {word} in form login {TestLocators.LOCATOR_LOGIN_FIELD[1]}')
        self.find_element(self.LOCATOR_LOGIN_FIELD).clear()
        self.find_element(self.LOCATOR_LOGIN_FIELD).send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Enter {word} in form login {TestLocators.LOCATOR_PASS_FIELD[1]}')
        self.find_element(self.LOCATOR_PASS_FIELD).clear()
        self.find_element(self.LOCATOR_PASS_FIELD).send_keys(word)

    def click_login_button(self):
        logging.info('Click button ')
        self.find_element(self.LOCATOR_BUTTON).click()

    def get_error_text(self):
        err_field = self.find_element(self.LOCATOR_ERR_FIELD, time=5)
        error_text = err_field.text
        logging.info(f'Error {error_text} ')
        return error_text

    def check_enter_user(self):
        user_name = self.find_element(TestLocators.LOCATOR_AUTH).text
        return user_name

    def button_contact(self):
        self.find_element(self.LOCATOR_CONTACT_BTN).click()

    def check_open_form(self):
        open_form = self.find_element(self.LOCATOR_TITLE_FORM)
        form_text = open_form.text
        return form_text

    def input_form_name(self, text):
        input_login = self.find_element(self.LOCATOR_NAME_INPUT)
        input_login.send_keys(text)

    def input_form_email(self, text):
        input_login = self.find_element(self.LOCATOR_E_MAIL)
        input_login.send_keys(text)

    def input_form_content(self, text):
        input_login = self.find_element(self.LOCATOR_CONTENT_INPUT)
        input_login.send_keys(text)

    def contact_us_btn(self):
        self.find_element(self.LOCATOR_CONTACTUS_BTN).click()

    def check_alert_text(self):
        try:
            alert_text = self.driver.switch_to.alert.text
            return alert_text
        except:
            return None
