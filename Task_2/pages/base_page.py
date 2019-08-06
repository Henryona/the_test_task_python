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
    
    def find_and_type(self, message, *locator):
        input_element = self.browser.find_element(*locator)
        input_element.send_keys(message)

    def is_element_present(self, *locator):
        try:
            self.browser.find_element(*locator)
        # перехватим исключение
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, *locator, timeout=4):
        # проверка, что элемент не появляется на странице в течение заданного времени
        try:
            wait(self.browser, timeout).until(EC.presence_of_element_located((*locator)))
        except TimeoutException:
            return True

    def product_name_should_match(self, first_name, second_name):
        assert first_name == second_name, "Названия товара не совпали, тест провален"

    def remember_info(self, *locator):
        return self.browser.find_element(*locator).text

'''Не используется в тесте: 
# эту штуку передать, но не вызывать (без () )
def for_wait_is_alert_present(browser):
        try:
            alert = browser.switch_to.alert
            alert.accept()
        except (NoAlertPresentException):
            return False
        return True

# эта штука вызовется сама только в нужном месте кода  (используется замыкание)
def for_wait_is_element_present(*locator):
    def inner(browser):
        try:
            return browser.find_element(*locator)
        except (NoSuchElementException):
            return False
        return True
    return inner

# класс: expected_condition, который дожидается алерта (оформление аналогичное оригинальным Expected Conditions из коробки)
class for_wait_is_alert_present(object):
    def __init__(self, *args, **kwargs):
        super(is_alert_present, self).__init__(*args, **kwargs)
	
    def __call__ (self, browser):
        try:
            alert = browser.switch_to.alert
            alert.accept()
        except (NoAlertPresentException):
            return False
        return True'''
    
