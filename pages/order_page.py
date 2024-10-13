from pages.base_page import BasePage
from pages_locators.order_page_locators import OrderPageLocators
from pages_locators.main_page_locators import MainPageLocators
import data
import allure


class OrderPage(BasePage):

    @allure.step('Открываем страницу заказа')
    def navigate_to_order_page(self, locator):
        self.open_page(data.HOMEPAGE_URL)
        self.accept_cookies(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(locator)

    @allure.step('Создаем заказ')
    def set_order(self, name, surname, address, metro_station, telephone_number, cell, comment):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_on_element(OrderPageLocators.METRO_STATION_DROPDOWN)
        self.click_on_element(metro_station)
        self.add_text_to_element(OrderPageLocators.TELEPHONE_NUMBER_INPUT, telephone_number)
        self.click_on_element(OrderPageLocators.APPLY_BUTTON)
        self.click_on_the_specific_cell_of_calendar(cell)
        self.click_on_element(OrderPageLocators.DURATION_DROPDOWN)
        self.click_on_element(OrderPageLocators.DURATION_SELECT)
        self.click_on_element(OrderPageLocators.COLOUR_SELECT)
        self.add_text_to_element(OrderPageLocators.COMMENT_SECTION, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Проверяем, что произошел переход по URL')
    def check_url(self, expected_url):
        return self.driver.current_url == expected_url

    def click_on_the_specific_cell_of_calendar(self, cell_index):
        self.click_on_element(OrderPageLocators.DATE_INPUT)
        formatted_specific_cell = self.format_locators(OrderPageLocators.SPECIFIC_CALENDAR_CELL, cell_index)
        self.click_on_element(formatted_specific_cell)

