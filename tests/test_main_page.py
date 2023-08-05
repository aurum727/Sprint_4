import allure
import pytest
from pages.page_main import MainPage
from urls import AdressSite
import data
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Проверка соответствия ответов на вопросы на главной странице.')
    @allure.description('Поочередно проверяем ответы на вопросы. Сверяем с эталонными из списка answer_list')
    @pytest.mark.parametrize('answer_number, answer_text', data.main_page_answers_list)
    def test_checking_answers(self, driver, answer_number, answer_text):
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        answer_from_page = main_page.get_answer_for_question_by_number(answer_number)
        assert answer_from_page == answer_text
