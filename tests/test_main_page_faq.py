import data
import allure
import pytest

from pages.main_page import MainPage
from pages_locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title("Проверка вопросов и ответов")
    @allure.description("Тест проверяет, что ответы на вопросы"
                        " соответствуют ожидаемым результатам")
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, data.ANSWER_1),
            (1, data.ANSWER_2),
            (2, data.ANSWER_3),
            (3, data.ANSWER_4),
            (4, data.ANSWER_5),
            (5, data.ANSWER_6),
            (6, data.ANSWER_7),
            (7, data.ANSWER_8)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_page(data.HOMEPAGE_URL)
        main_page.accept_cookies(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        assert main_page.get_answer_text(num) == result
