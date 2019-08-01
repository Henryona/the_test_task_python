'''
# Задание № 2: тестирование Yandex - маркета
# Входные данные: отсутствуют
# Выходные данные: вывод в консоль результатов прогона двух тестов.
# Успешный результат прохождения теста будет в том случае, если
# название товара в описании товара будет совпадать с названием этого 
# товара в превью в сетке результатов найденных товаров.
'''

from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import pytest

#@pytest.mark.parametrize()
def test_compare_product_names():
    link = BasePageLocators.YANDEX_PAGE_LINK
	page = YandexMainPage(browser,  link)

    # открываем нужную страницу
    page.open()
    page.find_and_click(YANDEX_MARKET_BUTTON)