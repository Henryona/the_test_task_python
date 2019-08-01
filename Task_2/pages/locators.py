from selenium.webdriver.common.by import By

class BasePageLocators():
    YANDEX_PAGE_LINK = "https://yandex.ru/"

class YandexMainPageLocators():
    YANDEX_MARKET_BUTTON = (By.CSS_SELECTOR, '[data-id="market"]')

class YaMarketPageLocators():
    MOBILE_PRICE_FROM = "40000"
    MOBILE_PRICE_TO = ""
    HEADPHONES_PRICE_FROM = "17000"
    HEADPHONES_PRICE_TO = "25000"
    CATEGORY_ELECTRONIC = (By.LINK_TEXT, "Электроника")
    SUBCATEGORY_MOBILE_PHONES = (By.LINK_TEXT, "Мобильные телефоны")
    SUBCATEGORY_HEADPHONES = (By.LINK_TEXT, "Наушники и Bluetooth-гарнитуры")
    MIN_PRICE_INPUT = (By.ID, "glpricefrom")
    MAX_PRICE_INPUT = (By.ID, "glpriceto")
    SAMSUNG_CHECKBOX = (By.ID, "7893318_153061")
    BEATS_CHECKBOX = (By.ID, "7893318_8455647")
    POP_UP_CONFIRM = (By.CLASS_NAME, "_1PQIIOelRL")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, "div.n-snippet-cell2__title a.link")

class ProductPageLocators():
    TITLE_PRODUCT_NAME = (By.CSS_SELECTOR, ".n-title__text h1")