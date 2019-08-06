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
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest

# тест запускается 2 раза с разными наборами параметров
@pytest.mark.parametrize( \
'subcategory, manufactor, price_from, price_to', [(YaMarketPageLocators.SUBCATEGORY_MOBILE_PHONES, YaMarketPageLocators.SAMSUNG_CHECKBOX, YaMarketPageLocators.MOBILE_PRICE_FROM, YaMarketPageLocators.MOBILE_PRICE_TO), (YaMarketPageLocators.SUBCATEGORY_HEADPHONES, YaMarketPageLocators.BEATS_CHECKBOX, YaMarketPageLocators.HEADPHONES_PRICE_FROM, YaMarketPageLocators.HEADPHONES_PRICE_TO)])
def test_compare_product_names(browser, subcategory, manufactor, price_from, price_to):
    link = BasePageLocators.YANDEX_PAGE_LINK
    page = YandexMainPage(browser,  link)

    # открываем нужную страницу и переходим в маркет
    page.open()
    page.find_and_click(*YandexMainPageLocators.YANDEX_MARKET_BUTTON)

    # подтверждаем алерт: "Вы находитесь в <название_города>", если он появился
    # на самом деле, он не алерт, а просто всплывающее окошко, к которому даже accept() не применить :с 
    try:
        alert = wait(browser, 10).until(EC.presence_of_element_located(YaMarketPageLocators.NOTIFICATION)) 
        alert.click()
    except:
        pass

    # переходим в раздел и затем в подраздел
    page.find_and_click(*YaMarketPageLocators.CATEGORY_ELECTRONIC)
    page.find_and_click(*subcategory)

    # выбираем производителя и устанавливаем мин\макс цену
    manufactor_checkbox = wait(browser, 10).until(EC.element_to_be_clickable(manufactor))
    manufactor_checkbox.click()
    wait(browser, 10).until(EC.visibility_of_element_located(YaMarketPageLocators.POP_UP_CONFIRM)) # ждём флага, что применился фильтр по производителю
    yamarket_page = YaMarketPage(browser, browser.current_url)
    yamarket_page.decide_what_need_to_type(price_from, *YaMarketPageLocators.MIN_PRICE_INPUT)
    yamarket_page.decide_what_need_to_type(price_to, *YaMarketPageLocators.MAX_PRICE_INPUT)

    # ожидание появления всплывающего флажка, показывающего, что фильтры применились
    wait(browser, 10).until(EC.visibility_of_element_located(YaMarketPageLocators.POP_UP_CONFIRM))

    # запоминаем название первого товара
    product_name_on_desk = page.remember_info(*YaMarketPageLocators.FIRST_PRODUCT_NAME)
    # print(product_name_on_desk)

    # переходим на страницу товара и запоминаем название товара в тайтле
    page.find_and_click(*YaMarketPageLocators.FIRST_PRODUCT_NAME)
    product_name_on_title = page.remember_info(*ProductPageLocators.TITLE_PRODUCT_NAME)

    # сраниваем имена товара
    page.product_name_should_match(product_name_on_desk, product_name_on_title)
