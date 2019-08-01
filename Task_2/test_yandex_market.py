'''
# Задание № 2: тестирование Yandex - маркета
# Входные данные: отсутствуют
# Выходные данные: вывод в консоль результатов прогона двух тестов.
# Успешный результат прохождения теста будет в том случае, если
# название товара в описании товара будет совпадать с названием этого 
# товара в превью в сетке результатов найденных товаров.
'''

from pages.yamarket_page_ import YaMarketPage
from pages.yandex_page import YandexMainPage
from pages.locators import BasePageLocators
from pages.locators import YandexMainPageLocators
from pages.locators import YaMarketPageLocators
from pages.locators import ProductPageLocators
import pytest

@pytest.mark.parametrize( \
'subcategory, manufactor, price_from, price_to', [(YaMarketPageLocators.SUBCATEGORY_MOBILE_PHONES, YaMarketPageLocators.SAMSUNG_CHECKBOX, YaMarketPageLocators.MOBILE_PRICE_FROM, YaMarketPageLocators.MOBILE_PRICE_TO), (YaMarketPageLocators.SUBCATEGORY_HEADPHONES, YaMarketPageLocators.BEATS_CHECKBOX, YaMarketPageLocators.HEADPHONES_PRICE_FROM, YaMarketPageLocators.HEADPHONES_PRICE_TO)])
def test_compare_product_names(browser, subcategory, manufactor, price_from, price_to):
    link = BasePageLocators.YANDEX_PAGE_LINK
    page = YandexMainPage(browser,  link)

    # открываем нужную страницу и переходим в маркет
    page.open()
    page.find_and_click(*YandexMainPageLocators.YANDEX_MARKET_BUTTON)

    # подтверждаем алерт: "Вы находитесь в ..."
    input()
    alert = browser.switch_to.alert
    alert.accept()

    # переходим в раздел и затем в подраздел
    page.find_and_click(*YaMarketPageocators.CATEGORY_ELECTRONIC)
    page.find_and_click(subcategory)

    # выбираем производителя и устанавливаем мин\макс цену
    page.wait_and_click(manufactor)
    page.decide_what_need_to_type(price_from, price_to)

    # ожидание появления всплывающего флажка, показывающего, что фильтр применился
    wait(driver, 10).until(EC.visibility_of_element_located(*YaMarketPageocators.POP_UP_CONFIRM))

    # запоминаем название первого товара
    product_name_on_desk = page.remember_info(*YaMarketPageocators.FIRST_PRODUCT_NAME)

    # переходим на страницу товара и запоминаем название товара в тайтле
    page.find_and_click(*YaMarketPageocators.FIRST_PRODUCT_NAME)
    product_name_on_title = page.remember_info(*ProductPageLocators.TITLE_PRODUCT_NAME)

    # сраниваем имена товара
    page.product_name_should_match(product_name_on_desk, product_name_on_title)