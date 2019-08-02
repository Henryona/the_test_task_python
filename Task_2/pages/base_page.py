from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
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

    '''def wait_and_click(self, *locator):
        waited_elememt = wait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        waited_element.click()'''
    
    def find_and_type(self, *locator, message):
        input_element = self.browser.find_element(locator)
        input_element.send_keys(message)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        # перехватим исключение
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # проверка, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

    def product_name_should_match(self, first_name, second_name):
        assert first_name == second_name, "Названия товара не совпали, тест провален"

    def remember_info(self, *locator):
        return self.browser.find_element(locator).text

# класс: expected_condition, который дожидается алерта 
class for_wait_is_alert_present(object):
    def __init__(self, *args, **kwargs):
        super(is_alert_present, self).__init__(*args, **kwargs)
	
    def __call__ (self, browser):
        try:
            alert = browser.switch_to.alert
            alert.accept()
        except (NoAlertPresentException):
            return False
        return True

class for_wait_is_element_present(object):
    def __init__(self, *locator):
        self.locator = locator
	
    def __call__ (self, browser):
        try:
            return browser.find_element(*self.locator)
        except (NoSuchElementException):
            return False
        return True

    
