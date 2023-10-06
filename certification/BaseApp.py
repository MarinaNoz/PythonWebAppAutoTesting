import logging
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def parse_locators(filename: str):
    ids = dict()
    with open(filename) as f:
        locators = yaml.safe_load(f)
    if 'xpath' in locators.keys():
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
    if 'css' in locators.keys():
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])
    return ids


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f'Cant find element by locator{locator}')
        except:
            logging.exception('Find element exсeptoin')
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'property {property} not found in element with {locator}')
            return None


    def go_to_site(self, url='https://test-stand.gb.ru'):
        try:
            start_browsing = self.driver.get(url)
        except:
            logging.exception('Exeption while open site')
            start_browsing = None
        return start_browsing


    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f' Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {element_name}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception while button click')
            return False
        logging.debug(f'Clicked {element_name}')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator)
        if not field:
            logging.error(f' Element {locator} not found')
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'Find text {text} in {field}')
        return text

    def click_about(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        about_button = self.find_element(locator)
        if not about_button:
            return False
        try:
            about_button.click()
        except:
            logging.exception(f'Exception while button click')
            return False
        logging.debug(f'Clicked {element_name}')
        return True
