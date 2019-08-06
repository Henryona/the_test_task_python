from .base_page import BasePage
from .locators import YaMarketPageLocators

class YaMarketPage(BasePage):

    def decide_what_need_to_type(self, price_number, *locator):
        if price_number is not "":
            self.find_and_type(price_number, *locator)
