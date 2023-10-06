from BaseApp import BasePage
from BaseApp import parse_locators
from selenium.webdriver.common.by import By
import logging
import yaml

ids = parse_locators('locators.yaml')


class OperationsHelper(BasePage):

    def enter_login(self, word):
        self.enter_text_into_field(ids['LOCATOR_LOGIN_FIELD'], word, 'login_field')

    def enter_pass(self, word):
        self.enter_text_into_field(ids['LOCATOR_PASS_FIELD'], word, 'pass_field')

    def click_login_button(self):
        self.click_button(ids['LOCATOR_LOGIN_BTN'], 'login_btn')

    def get_err_text(self):
        return self.get_text_from_element(ids['LOCATOR_ERR_FIELD'], 'login_error')

    def auth(self):
        return self.find_element(ids['LOCATOR_AUTH_FIELD']).text

    def click_about(self):
        self.click_button(ids['LOCATOR_ABOUT_FIELD'])

    def about(self):
        return self.find_element(ids['LOCATOR_ABOUT_TEXT_FIELD']).text

    def about_size(self):
        return self.find_element(ids['LOCATOR_ABOUT_TEXT_FIELD']).value_of_css_property("font-size")
