import data
import allure

from pages.order_page import OrderPage
from pages_locators.order_page_locators import OrderPageLocators
from pages_locators.main_page_locators import MainPageLocators


class TestOrderPage:

    @allure.title('Проверка создания заказа и перехода на домашнюю страницу')
    @allure.description(
        "Тест создания заказа через верхнюю кнопку 'Заказать' и последующего клика по логотипу самоката "
        "для проверки перенаправления на главную страницу.")
    def test_making_order_then_click_on_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.navigate_to_order_page(MainPageLocators.ORDER_UPPER_BUTTON)
        order_page.set_order(
            data.NAME_1,
            data.SURNAME_1,
            data.ADDRESS_1,
            OrderPageLocators.METRO_STATION_1,
            data.TELEPHONE_NUMBER_1,
            data.CELL_1,
            data.COMMENT_1
        )
        order_done_text = order_page.check_order(OrderPageLocators.ORDER_DONE_HEADER)
        assert data.ORDER_DONE_TEXT in order_done_text
        order_page.click_on_element(OrderPageLocators.CHECK_STATUS_BUTTON)
        order_page.click_on_element(OrderPageLocators.SCOOTER_LOGO)
        assert order_page.check_url(data.HOMEPAGE_URL)

    @allure.title("Проверка создания заказа и перехода на страницу Dzen")
    @allure.description("Тест создания заказа через нижнюю кнопку 'Заказать' и последующего клика по логотипу Яндекса "
                        "для проверки перенаправления на страницу Дзен.")
    def test_making_order_then_click_on_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.navigate_to_order_page(MainPageLocators.ORDER_LOWER_BUTTON)
        order_page.set_order(
            data.NAME_2,
            data.SURNAME_2,
            data.ADDRESS_2,
            OrderPageLocators.METRO_STATION_2,
            data.TELEPHONE_NUMBER_2,
            data.CELL_2,
            data.COMMENT_2
        )
        order_done_text = order_page.check_order(OrderPageLocators.ORDER_DONE_HEADER)
        assert data.ORDER_DONE_TEXT in order_done_text
        order_page.click_on_element(OrderPageLocators.CHECK_STATUS_BUTTON)
        order_page.click_on_element(OrderPageLocators.YANDEX_LOGO)
        order_page.switch_to_next_tab(data.DZEN_URL)
        assert order_page.check_url(data.DZEN_URL)
