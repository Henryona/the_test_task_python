from selenium.webdriver.common.by import By

class BasePageLocators():
    YANDEX_PAGE_LINK = "https://yandex.ru/"

class YandexMainPageLocators():
    YANDEX_MARKET_BUTTON = (By.CSS_SELECTOR, '[data_id="market"]')