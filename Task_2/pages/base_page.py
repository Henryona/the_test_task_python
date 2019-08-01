from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage(object):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
		
    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def find_and_click(self, *locator):
        element = self.browser.find_element(*locator)
        element.click()

    def wait_and_click(self, *locator):
        waited_elememt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        waited_element.click()
    
    def find_and_type(self, *locator, message):
        input_element = self.browser.find_element(locator)
        input_element.send_keys(message)

    def product_name_should_match(self, first_name, second_name):
        assert first_name == second_name, "Названия товара не совпали, тест провален"

    def remember_info(self, *locator):
        return self.browser.find_element(locator).text
	