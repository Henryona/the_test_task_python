from .base_page import BasePage
from .locators import YaMarketPageLocators

class YaMarketPage(BasePage):

    def decide_what_need_to_type(price_from, price_to):
        if price_from is not null:
            page.find_and_type(*YaMarketPageocators.MIN_PRICE_INPUT, YaMarketPageocators.MOBILE_PRICE_FROM)
        if price_to is not null:
            page.find_and_type(*YaMarketPageocators.MAX_PRICE_INPUT, YaMarketPageocators.MOBILE_PRICE_TO)